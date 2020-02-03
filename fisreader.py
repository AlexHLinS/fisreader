from sys import argv, exit
import csv
# import parameter's name aliases
from paramnames import log_param_names

param_count = 0
param_names = []
param_values = []

# opening file method
def logopen(logfilename):
    try:
        with open(logfilename,"rb") as log:
            param_count = ord(log.read(1)) # get param count
            print("Param count =", param_count)

            # get names
            for i in range(param_count):
                buf = log.read(2)
                key = int.from_bytes(buf, byteorder='little')
                param_names.append(log_param_names[key])
                print('added', i,' element')

            log.seek((6+param_count*2),0) # go to DATA section on file
            #log.seek(124,0) # go to DATA section on file
            buf = 0x01 # init buffer value
            j = 0 # points count
            while buf: # repeat while buff not NULL
                params_v = [] # temp list of data values

                for i in range(param_count): # read one data set
                    buf = log.read(2) # read one value
                    params_v.append(int.from_bytes(buf, byteorder='little')) # put it to the temp list

                param_values.append(params_v) # append temp list to values list
                j += 1

            param_values.pop(-1) # cut last zero valued element
            print(param_values) # print it for shure
            print("Found", j,"points with", param_count,"variables!") # show statistics
            print("Names:", param_names)
    except:
        return False # if error occure - return False
    return True


def csvgen():
    with open(argv[1]+'.csv', 'w', newline='') as csv_out:
        csv_writer = csv.writer(csv_out, dialect='excel')
        csv_writer.writerow(param_names)
        for i in range(len(param_values)):
            csv_writer.writerow(param_values[i-1])
    csv_out.close()
    return


# main method
def main():
    # checking execute string
    if len(argv) != 2:
        print("Usage: python fisreader.py datalogfilename")
        exit(1)

    # error of opening file
    if not logopen(argv[1]):
        print("error opening file", argv[1])
        exit(2)

    csvgen()

    return


if __name__ == "__main__":
    main()