#
# Main F-Con iS Log files (*.LIS) tool module
#
# This module works with F-Con iS Log files (*.LIS)
# and provide base functionality
#
# Author: Alex Shkil aka HLinS
#

from sys import argv, exit
import csv
# import parameter's name aliases
from paramnames import log_param_names
# import fuel and ignition calculations module

import fi_calculations

param_count = int(0)
param_names = list([])
param_values = list([])


# opening file method
def log_open(log_file_name):
    global param_count
    try:
        with open(log_file_name, "rb") as log:
            param_count = ord(log.read(1))  # get param count
            print("Param count =", param_count)

            # get names
            for i in range(param_count):
                buf = log.read(2)  # temp variable for red data
                # encrypt data to int
                key = int.from_bytes(buf, byteorder='little')
                param_names.append(log_param_names[key])  # add name got by int
                # print('added', i,' element') # debug sake console output

            # go to DATA section on file (header 6 bytes + parameters list (param_count)*2 bytes)
            log.seek((6+param_count*2), 0)
            # log.seek(124,0) # go to DATA section on file
            buf = 0x01  # init buffer value
            j = 0  # points count
            while buf:  # repeat while buff not NULL
                params_v = []  # temp list of data values

                for i in range(param_count):  # read one data set
                    buf = log.read(2)  # read one value
                    # put it to the temp list
                    params_v.append(int.from_bytes(buf, byteorder='little'))

                # append temp list to values list
                param_values.append(params_v)
                j += 1

            param_values.pop(-1)  # cut last zero valued element
            # print(param_values)  # print it for sure
            print("Found", j, "points with", param_count,
                  "variables!")  # show statistics
            # print("Names:", param_names) # debug sake

            param_value_normaliser(param_names, param_values)
    except Exception as e:
        print(f'Error: {e}')
        return False  # if error occur - return False
    return True


def param_value_normaliser(parameters_names, parameters_values):
    for i in range(len(parameters_values)):
        for j in range(len(parameters_names)):
            # checking and "fixing" negative values, in log
            # negative values represented as "max(USHRT_MAX) + value"
            # for example, -5 => USHRT_MAX + (-5) = 65535 - 5 = 65530
            if parameters_values[i][j] > 65000:
                parameters_values[i][j] = parameters_values[i][j] - 65535
            # checking and "fixing" A/F values, these represented as A/F*100:
            # for example, 14,7 => A/F*100 = 1470
            if (parameters_names[j] == log_param_names[3328]) or (parameters_names[j] == log_param_names[8704]):
                parameters_values[i][j] = float(parameters_values[i][j] / 100)
    return 1


def csv_gen():
    with open(argv[1]+'.csv', 'w', newline='') as csv_out:
        csv_writer = csv.writer(csv_out, dialect='excel')
        csv_writer.writerow(param_names)
        for i in range(len(param_values)):
            csv_writer.writerow(param_values[i-1])
    csv_out.close()
    print('All data put in ->', csv_out.name)
    return


def afr_cal_csv():
    pf = 4.0
    gf = 0.740
    injf = 370
    injf_p = 3.05

    with open(argv[1]+'_AFRcal.csv', 'w', newline='') as csv_out:
        csv_writer = csv.writer(csv_out, dialect='excel')
        csv_writer.writerow(['MAF', 'Voltage'])
        for i in range(len(param_values)):
            pi = param_names.index('Pressure, mm Hg')
            map_value = fi_calculations.mm_hg_to_m_pa(param_values[i][pi])
            ai = param_names.index('A/F')
            af = param_values[i][ai]
            ti = param_names.index('Fuel: Main output, usec')
            t = param_values[i][ti]
            fr = fi_calculations.calc_inj_flow(pf, map_value, injf, injf_p)
            fm = fi_calculations.calc_fuel_mass(fr, gf, t)
            maf = fi_calculations.calc_air_mass_from_afr(fm, af/100)

            ait = param_values[i][param_names.index(
                'Intake air temp, deg C')] + 273.15

            dest = (map_value * 1000) / (ait + 287.058)  # kg/m3

            vi = param_names.index('AirFlow#1 output, mV')

            if dest != 0:
                vaf = maf / dest / 1000  # MPa / kg / m3 -> m3
                csv_writer.writerow([vaf, param_values[i][vi]])

    csv_out.close()
    print('All af calibration data put in ->', csv_out.name)
    return

# main method


def main():
    # checking execute string
    if len(argv) != 2:
        print("Usage: python fisreader.py datalog_filename")
        exit(1)

    # error of opening file
    if not log_open(argv[1]):
        print("error opening file", argv[1])
        exit(2)

    csv_gen()
    afr_cal_csv()

    return


if __name__ == "__main__":
    main()
