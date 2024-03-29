#
# F-Con iS log file parameter names aliases
#
# This module provides aliases for parameter names
#
# Author: Alex Shkil aka HLinS
#

# Parameter's names
log_param_names = {
    256: 'RPM',
    512: 'Pressure(mm Hg)',
    768: 'Throttle(%)',
    1024: 'Throttle differential(%)',
    1280: 'AirFlow#1 input(mV)',
    1536: 'AirFlow#2 input(mV)',
    1792: 'AirFlow input average(mV)',
    2048: 'AirFlow input Karman(Hz)',
    2304: 'AirFlow#1 output(mV)',
    2560: 'AirFlow#2 output(mV)',
    2816: 'AirFlow output Karman(Hz)',
    3072: 'Car speed(km/h)',
    3328: 'A/F',
    3584: 'Fuel: Main input(usec)',
    3840: 'Fuel: Sub input #1(usec)',
    4096: 'Fuel: Sub input #2(usec)',
    4352: 'Injector dead time(usec)',
    4608: 'Fuel: Main output(usec)',
    4864: 'Fuel: Sub output #1(usec)',
    5120: 'Fuel: Sub output #2(usec)',
    5376: 'Injector output dead time(usec)',
    5632: 'AIC output(usec)',
    5888: 'AIC main map(usec)',
    6144: 'AIC dead time(usec)',
    6400: 'Battery(mV)',
    6656: 'Option output #1(usec)',
    6912: 'Option output #2(usec)',
    7168: 'Coolant temp(deg C)',
    7424: 'Intake air temp(deg C)',
    7680: 'Knock level',
    7936: 'NVCS',
    8192: 'EIDS time(usec)',
    8448: 'EIDS',
    8704: 'Target A/F',
    8960: 'Trim: Fuel: Sum',
    9216: 'Trim: Ignition: Sum',
    9472: 'Trim: AIC: Sum',
    9728: 'Trim: Fuel: A',
    9984: 'Trim: Fuel: B',
    10240: 'Trim: Fuel: Water temp',
    10496: 'Trim: Fuel: Intake air temp',
    10752: 'Trim: Fuel: GCC',
    11008: 'Trim: Fuel: VPC',
    11264: 'Trim: Fuel: Scramble',
    11520: 'Trim: Fuel: Acceleration',
    11776: 'Trim: Ignition: A',
    12032: 'Trim: Ignition: B',
    12288: 'Trim: Ignition: Water temp',
    12544: 'Trim: Ignition: Intake air temp',
    12800: 'Trim: Ignition: GCC',
    13056: 'Trim: Ignition: VPC',
    13312: 'Trim: Ignition: Scramble',
    13568: 'Trim: Ignition: Acceleration',
    13824: 'Trim: AIC: Water temp',
    14080: 'Trim: AIC: Air temp',
    14336: 'Scramble time',
    14592: 'Ignition: Shift up',
    14848: 'Ignition: Shift down',
    15104: '(OBD) Close-loop cancellation',
    15360: '(OBD) Ignition timing input #1',
    15616: '(OBD) A/F Trim #1',
    15872: '(OBD) A/F Study #1',
    16128: '(OBD) Ignition timing input #2',
    16384: '(OBD) A/F Trim #2',
    16640: '(OBD) A/F Study #2',
    16896: '(OBD) Control condition',
    17152: '(OBD) Ignition timing output #1',
    17408: 'I/F boost',
    18944: '(OBD) Ignition timing output #2'
}
