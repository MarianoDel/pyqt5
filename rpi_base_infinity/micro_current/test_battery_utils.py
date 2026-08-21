# use python3

from battery_utils import BatteryCharge_With_Mains, BatteryCharge_With_Batt, BatteryCharge_Filter, BatteryCharge_Filter_Reset, BatteryCharge_Total_Charge_To_Percent


print('Tests battery utils module')

print('Mains connected')
batt_volts = 8.4
charge = BatteryCharge_With_Mains (batt_volts)

print(f'with batt volts: {batt_volts} charge: {charge}')

batt_volts = 7.3
charge = BatteryCharge_With_Mains (batt_volts)

print(f'with batt volts: {batt_volts} charge: {charge}')


print('\nBatt connected')
batt_volts = 8.2
charge = BatteryCharge_With_Batt (batt_volts)

print(f'with batt volts: {batt_volts} charge: {charge}')

batt_volts = 7.1
charge = BatteryCharge_With_Batt (batt_volts)

print(f'with batt volts: {batt_volts} charge: {charge}')


print('\nBatt filter tests')
BatteryCharge_Filter_Reset()

charge = 9000.0
total_charge = 0.0
for x in range(10):
    total_charge = BatteryCharge_Filter(charge)
    print(f'filter charge: {total_charge}')


print('\nSecond Batt filter tests')
BatteryCharge_Filter_Reset()

batt_str_list = [7.6, 7.76, 7.76, 7.75]
total_charge = 0.0
for x in range(4):            
    total_charge += BatteryCharge_With_Batt(float(batt_str_list[x]))

print(f'total charge: {total_charge} for voltages: {batt_str_list}')

total_charge_filter = 0.0
for x in range(10):
    total_charge_filter = BatteryCharge_Filter(total_charge)

percent = BatteryCharge_Total_Charge_To_Percent(total_charge_filter)    
print(f'filter charge: {total_charge_filter} percent: {percent}')    

print('\nThird Batt filter tests')
BatteryCharge_Filter_Reset()

batt_str_list = [7.55, 7.72, 7.74, 7.69]
total_charge = 0.0
for x in range(4):            
    total_charge += BatteryCharge_With_Batt(float(batt_str_list[x]))

print(f'total charge: {total_charge} for voltages: {batt_str_list}')

total_charge_filter = 0.0
for x in range(10):
    total_charge_filter = BatteryCharge_Filter(total_charge)

percent = BatteryCharge_Total_Charge_To_Percent(total_charge_filter)    
print(f'filter charge: {total_charge_filter} percent: {percent}')    


