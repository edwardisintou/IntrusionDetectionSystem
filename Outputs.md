### Question 1: Import data
#### Test case 1:\
data = get_data("proj1_data0.csv")\
print(data[0]) #gets the headers
- Output 1:\
['Timestamp', 'Arbitration_ID', 'DLC', 'Data', 'Class', 'SubClass']

#### Test case 2:\
data = get_data("proj1_data0.csv")\
print(data[10])
- Output 2:\
['1597759710.128601', '453', '5', '00 88 8B 00 C1', 'Normal', 'Normal']

#### Test case 3:\
data = get_data("proj1_data3_small.csv")\
print(data[50])
- Output 3:\
['1597759356.2377900', '8', '381', '80 C8 3F 00 00 F6 3C 05', 'Normal', 'Normal']

### Question 2: Find unique IDs
#### Test case 1:\
data = get_data("proj1_data0.csv")\
uids = unique_id(data)\
print(uids[0])\
- Output 1:\
000

#### Test case 2:\
data = get_data("proj1_data0.csv")\
uids = unique_id(data)\
print(uids[5])
- Output 2:\
153

#### Test case 3:\
data = get_data("proj1_data3_small.csv")\
uids = unique_id(data)\
print(uids[-1])
- Output 3:\
5CD
