### Question 1: Import data
- Test case 1:\
data = get_data("proj1_data0.csv")\
print(data[0]) #gets the headers
- Output 1:\
['Timestamp', 'Arbitration_ID', 'DLC', 'Data', 'Class', 'SubClass']

- Test case 2:\
data = get_data("proj1_data0.csv")
print(data[10])
- Output 2:\
['1597759710.128601', '453', '5', '00 88 8B 00 C1', 'Normal', 'Normal']