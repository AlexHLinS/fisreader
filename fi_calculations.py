#
# Fuel and Ignition parameters calculation module
#
# This module provide methods for different fuel and
# ignition parameters calculations
#
# Author: Alex Shkil aka HLinS
#
from math import sqrt


# Calculation Injector Flow from known flow and current differential pressure
def calc_inj_flow(fuel_press, manifould_press, known_flow, known_flow_dif_press):

    # calc current differentioal pressure
    differential_pressure = float(fuel_press) - float(manifould_press)

    cur_flow = float(known_flow) * sqrt(differential_pressure / float(known_flow_dif_press))

    return cur_flow

def calc_fuel_mass(flow, gravity, timing):
    # specific gravity of pump gas = 0.740 g/cm3
    # flow - in cc/min -> flow / 60 - сс/sec -> flow/60000 - cc/msec

    mass = (float(flow) / 6000) * float(gravity) * float(timing)

    return mass

def calc_air_mass_from_afr(fuel_mass, afr):
    air_mass = float(fuel_mass) * float(afr)
    return air_mass


def mmHg_to_mPa(pressure):
    result = float(pressure) / 7501
    return result

def main():

    Pf = input('Fuel pressure in rail in kPaX100:')
    MAP = input('MAP in mmHg:')
    Injf = input('Injector flow in cc/min:')
    InjfP = input('Differential pressure, where Inj produce this cc/min:')
    Gf = input('Specific gravity of fuel g/cm3:')
    AFR = input('AFR:')
    T = input('Timing, usec:')

    cif = calc_inj_flow(Pf, mmHg_to_mPa(MAP), Injf, InjfP)
    print("Current inj flow is:", cif, 'cc/min')
    fm = calc_fuel_mass(cif, Gf, T)
    print("Current fuel mass:", fm, 'g')
    afm = calc_air_mass_from_afr(fm, AFR)
    print("Current air mass:", afm, 'g')
    return

if __name__ == "__main__":
    main()