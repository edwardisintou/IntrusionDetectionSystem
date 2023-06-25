### Question 1: Import data
#### Test case 1:
data = get_data("proj1_data0.csv")\
print(data[0]) #gets the headers
- Output:\
['Timestamp', 'Arbitration_ID', 'DLC', 'Data', 'Class', 'SubClass']

#### Test case 2:
data = get_data("proj1_data0.csv")\
print(data[10])
- Output:\
['1597759710.128601', '453', '5', '00 88 8B 00 C1', 'Normal', 'Normal']

#### Test case 3:
data = get_data("proj1_data3_small.csv")\
print(data[50])
- Output:\
['1597759356.2377900', '8', '381', '80 C8 3F 00 00 F6 3C 05', 'Normal', 'Normal']

### Question 2: Find unique IDs
#### Test case 1:
data = get_data("proj1_data0.csv")\
uids = unique_id(data)\
print(uids[0])
- Output:\
000

#### Test case 2:
data = get_data("proj1_data0.csv")\
uids = unique_id(data)\
print(uids[5])
- Output:\
153

#### Test case 3:
data = get_data("proj1_data3_small.csv")\
uids = unique_id(data)\
print(uids[-1])
- Output:\
5CD

### Question 3: Retrieve relevant data
#### Test case 1:
data = get_data("proj1_data0.csv")\
edata = ecu_data('153', data)\
print(edata[0])
- Output:\
['1597759710.1258929', '153', '8', '20 A1 10 FF 00 FF 50 1F', 'Normal', 'Normal']

#### Test case 2:
data = get_data("proj1_data0.csv")\
edata = ecu_data('153', data)\
print(edata[22])
- Output:\
['1597759710.345933', '153', '8', '20 A1 10 FF 00 FF C0 8F', 'Normal', 'Normal']

#### Test case 3:
data = get_data("proj1_data3_small.csv")\
edata = ecu_data('368', data)\
print(edata[1])
- Output:\
['1597759356.234800', '8', '368', '00 00 00 00 00 FA 0A 40', 'Normal', 'Normal']

### Question 4: Measuring the time intervals
#### Test case 1:
data = get_data("proj1_data0.csv")\
interval = ecu_time_interval('153', data)\
print(round(interval[0], 5))
- Output:\
0.01005

#### Test case 2:
data = get_data("proj1_data0.csv")\
interval = ecu_time_interval('153', data)\
for i in range(10):\
    print(round(interval[i], 5))
- Output:\
0.01005\
0.01023\
0.00977\
0.01015\
0.00987\
0.00982\
0.0102\
0.0098\
0.01019\
0.00978

#### Test case 3:
data = get_data("proj1_data3_small.csv")
interval = ecu_time_interval('367', data)
print(round(interval[1], 5))
- Output:\
0.0102