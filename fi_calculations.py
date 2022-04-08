#
# Fuel and Ignition parameters calculation module
#
# This module provides methods for different fuel and
# ignition parameters calculations
#
# Author: Alex Shkil aka HLinS
#
from math import sqrt


# Calculation Injector Flow from known flow and current differential pressure
def calc_inj_flow(fuel_press, manifould_press, known_flow, known_flow_dif_press):
    # calc current differential pressure
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


def mm_hg_to_m_pa(pressure):
    result = float(pressure) / 7501
    return result


def main():
    pf = input('Fuel pressure in rail in kPaX100:')
    map_value = input('MAP in mmHg:')
    injf = input('Injector flow in cc/min:')
    injf_p = input('Differential pressure, where Inj produce this cc/min:')
    gf = input('Specific gravity of fuel g/cm3:')
    afr = input('AFR:')
    t = input('Timing, usec:')

    cif = calc_inj_flow(pf, mm_hg_to_m_pa(map_value), injf, injf_p)
    print("Current inj flow is:", cif, 'cc/min')
    fm = calc_fuel_mass(cif, gf, t)
    print("Current fuel mass:", fm, 'g')
    afm = calc_air_mass_from_afr(fm, afr)
    print("Current air mass:", afm, 'g')
    return


if __name__ == "__main__":
    main()
