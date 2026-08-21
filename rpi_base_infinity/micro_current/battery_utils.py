# use python3

############################
# Battery useful functions #
############################

def BatteryCharge_With_Mains (batt_volt):
    if batt_volt > 8.4:
        batt_volt = 8.4

    if batt_volt < 7.3:
        batt_volt = 7.3

    batt_volt = batt_volt - 7.3    # delta x = 1
    batt_mca = batt_volt * 8182    # delta y = 9000 mca is the max charge
    if batt_mca > 9000:
        batt_mca = 9000
        
    return batt_mca


def BatteryCharge_With_Batt (batt_volt):
    if batt_volt > 8.2:
        batt_volt = 8.2

    # no go to negative
    if batt_volt < 7.1:
        batt_volt = 7.1

    batt_volt = batt_volt - 7.1    # delta x = 1.1
    batt_mca = batt_volt * 8182    # delta y = 9000 mca is the max charge
    if batt_mca > 9000:
        batt_mca = 9000

    return batt_mca


charge_float_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
def BatteryCharge_Filter_Reset ():
    for x in range(10):
        charge_float_list[x] = 0.0


def BatteryCharge_Filter (new_charge):
    tot = new_charge

    for x in range(9):
        tot = tot + charge_float_list[x]

    for x in range(9):
        charge_float_list[9 - x] = charge_float_list[8 - x]

    charge_float_list[0] = new_charge
    return (tot / 10)


def BatteryCharge_Total_Charge_To_Percent (total_charge):
    total_perc = total_charge * 100 / (4 * 9000)
    total_perc_int = int(total_perc)
    return total_perc_int

