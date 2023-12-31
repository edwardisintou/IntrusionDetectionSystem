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

### Question 5: Summarising the statistics
#### Test case 1:
data = get_data("proj1_data0.csv")\
stat = ecu_summary(data)
- Output:\
ID  Count    Min TS    Avg TS    Max TS     SD TS\
 000   3621    0.0005    0.0008    0.0010    0.0001\
 043     40    0.9984    0.9992    1.0000    0.0003\
 07F     40    0.9995    1.0000    1.0006    0.0002\
 130   4011    0.0095    0.0100    0.0105    0.0001\
 140   4011    0.0095    0.0100    0.0105    0.0001\
 153   4014    0.0088    0.0100    0.0112    0.0001\
 164   4013    0.0092    0.0100    0.0108    0.0002\
 220   4014    0.0084    0.0100    0.0114    0.0004\
 251   4013    0.0090    0.0100    0.0110    0.0002\
 260   4013    0.0084    0.0100    0.0116    0.0004\
 2B0   4013    0.0088    0.0100    0.0112    0.0002\
 329   4013    0.0064    0.0100    0.0134    0.0008\
 340   4013    0.0087    0.0100    0.0113    0.0002\
 356   4014    0.0065    0.0100    0.0124    0.0005\
 366   4014    0.0073    0.0100    0.0127    0.0006\
 367   4014    0.0082    0.0100    0.0118    0.0005\
 368   4014    0.0081    0.0100    0.0119    0.0005\
 381   2006    0.0186    0.0200    0.0214    0.0003\
 386   2007    0.0156    0.0200    0.0244    0.0002\
 387   2006    0.0149    0.0200    0.0249    0.0006\
 389   2006    0.0145    0.0200    0.0262    0.0008\
 38D   2006    0.0186    0.0200    0.0212    0.0002\
 391   2007    0.0167    0.0200    0.0230    0.0003\
 394   2006    0.0172    0.0200    0.0228    0.0005\
 410    201    0.1993    0.2000    0.2004    0.0001\
 412    201    0.1991    0.2000    0.2004    0.0002\
 420   2006    0.0171    0.0200    0.0229    0.0005\
 421   2006    0.0177    0.0200    0.0227    0.0004\
 42D    402    0.0983    0.1000    0.1025    0.0003\
 436    802    0.0483    0.0500    0.0517    0.0006\
 44E    201    0.1989    0.2000    0.2011    0.0003\
 453   2007    0.0183    0.0200    0.0213    0.0004\
 470   2007    0.0187    0.0200    0.0215    0.0004\
 479    402    0.0984    0.1000    0.1008    0.0002\
 47F   2007    0.0165    0.0200    0.0238    0.0005\
 483    200    0.1982    0.2000    0.2017    0.0004\
 484    573    0.0628    0.0700    0.0772    0.0013\
 485    803    0.0428    0.0500    0.0571    0.0014\
 48A    803    0.0414    0.0500    0.0587    0.0020\
 48C    201    0.1962    0.2000    0.2048    0.0008\
 490    803    0.0416    0.0500    0.0584    0.0014\
 492    803    0.0444    0.0500    0.0558    0.0023\
 495    401    0.0973    0.1001    0.1031    0.0005\
 49F    201    0.1981    0.2000    0.2018    0.0005\
 4A2     80    0.4973    0.5001    0.5028    0.0007\
 4A7     81    0.4957    0.5001    0.5037    0.0008\
 4A9    201    0.1992    0.2000    0.2011    0.0002\
 4C9    201    0.1982    0.2000    0.2007    0.0002\
 4CB    201    0.1981    0.2000    0.2005    0.0002\
 4F1   2007    0.0152    0.0200    0.0246    0.0005\
 500    401    0.0975    0.1001    0.1026    0.0005\
 507    402    0.0972    0.1000    0.1029    0.0003\
 50A    200    0.1944    0.2000    0.2051    0.0008\
 50C    401    0.0961    0.1000    0.1039    0.0008\
 50E    201    0.1995    0.2000    0.2008    0.0001\
 520    401    0.0899    0.1000    0.1103    0.0014\
 52A    281    0.0186    0.1427    0.2028    0.0719\
 53B    201    0.1980    0.2000    0.2008    0.0002\
 53E    402    0.0956    0.1000    0.1045    0.0007\
 53F    201    0.1993    0.2000    0.2011    0.0002\
 541    401    0.0992    0.1000    0.1012    0.0002\
 544    201    0.1990    0.2000    0.2014    0.0002\
 553    201    0.1990    0.2000    0.2017    0.0002\
 559    201    0.1992    0.2000    0.2022    0.0002\
 563     67    0.5991    0.6000    0.6006    0.0002\
 568    402    0.0983    0.1000    0.1017    0.0007\
 572    201    0.1897    0.2000    0.2122    0.0015\
 57F     20    1.9989    2.0000    2.0010    0.0004\
 58B    803    0.0399    0.0500    0.0602    0.0027\
 593    200    0.1976    0.2000    0.2025    0.0006\
 5A6    201    0.1976    0.2000    0.2018    0.0003\
 5B0     40    0.9956    0.9998    1.0035    0.0013\
 5BE     40    0.9982    1.0000    1.0011    0.0004\
 5CD    200    0.1964    0.2000    0.2035    0.0007

#### Test case 2:
data = get_data("proj1_data0.csv")\
stat = ecu_summary(data, False)\
print(stat[0][:2])\
for val in stat[0][2:]:\
    print(f"{val:.10f}")
- Output:\
('000', 3621)\
0.0004801750\
0.0007825989\
0.0010421276\
0.0001047253

#### Test case 3:
data = get_data("proj1_data3_small.csv")\
stat = ecu_summary(data)
- Output:\
ID  Count    Min TS    Avg TS    Max TS     SD TS\
   0   1635    0.0004    0.0008    0.0010    0.0001\
 130    141    0.0095    0.0100    0.0104    0.0002\
 140    141    0.0095    0.0100    0.0104    0.0002\
 153    141    0.0095    0.0100    0.0105    0.0003\
 164    140    0.0095    0.0100    0.0105    0.0002\
 220    141    0.0093    0.0100    0.0109    0.0004\
 251    140    0.0096    0.0100    0.0105    0.0002\
 260    140    0.0074    0.0100    0.0133    0.0008\
 2B0    140    0.0091    0.0100    0.0108    0.0003\
 329    140    0.0063    0.0100    0.0125    0.0011\
 340    141    0.0095    0.0100    0.0105    0.0002\
 356    140    0.0091    0.0100    0.0109    0.0004\
 366    140    0.0089    0.0100    0.0110    0.0004\
 367    140    0.0089    0.0100    0.0108    0.0004\
 368    140    0.0090    0.0100    0.0110    0.0004\
 381     70    0.0192    0.0200    0.0211    0.0003\
 386     70    0.0185    0.0200    0.0214    0.0006\
 387     70    0.0185    0.0200    0.0215    0.0005\
 389     70    0.0157    0.0200    0.0243    0.0012\
 38D     70    0.0196    0.0200    0.0204    0.0002\
 391     70    0.0180    0.0200    0.0220    0.0008\
 394     70    0.0171    0.0200    0.0229    0.0016\
 410      7    0.1998    0.2000    0.2001    0.0001\
 412      7    0.1998    0.2000    0.2003    0.0002\
 420     70    0.0191    0.0200    0.0211    0.0003\
 421     70    0.0184    0.0200    0.0216    0.0006\
 42D     14    0.0997    0.1001    0.1014    0.0004\
 436     28    0.0496    0.0500    0.0508    0.0003\
 44E      7    0.1999    0.2001    0.2003    0.0001\
 453     70    0.0189    0.0200    0.0210    0.0005\
 470     70    0.0173    0.0200    0.0230    0.0011\
 479     14    0.0995    0.1000    0.1007    0.0004\
 47F     70    0.0186    0.0200    0.0214    0.0004\
 483      7    0.1998    0.2000    0.2003    0.0002\
 484     20    0.0671    0.0701    0.0728    0.0018\
 485     28    0.0473    0.0500    0.0527    0.0019\
 48A     28    0.0491    0.0500    0.0507    0.0003\
 48C      7    0.1972    0.1996    0.2024    0.0022\
 490     28    0.0478    0.0501    0.0526    0.0017\
 492     28    0.0488    0.0501    0.0522    0.0009\
 495     14    0.0998    0.1001    0.1005    0.0002\
 49F      7    0.1999    0.2005    0.2029    0.0012\
 4A2      3    0.4998    0.5002    0.5006    0.0006\
 4A9      7    0.1995    0.2001    0.2005    0.0004\
 4C9      7    0.1998    0.2001    0.2004    0.0002\
 4CB      7    0.1993    0.2001    0.2006    0.0005\
 4F1     71    0.0190    0.0200    0.0211    0.0005\
 500     14    0.0974    0.1001    0.1027    0.0011\
 507     15    0.0997    0.1000    0.1003    0.0001\
 50A      7    0.1970    0.2003    0.2031    0.0020\
 50C     14    0.0996    0.1001    0.1013    0.0005\
 50E      7    0.1997    0.2005    0.2028    0.0012\
 520     14    0.0953    0.1004    0.1049    0.0043\
 52A      7    0.1997    0.2000    0.2003    0.0002\
 53B      7    0.1996    0.2001    0.2006    0.0004\
 53E     14    0.0922    0.1007    0.1086    0.0057\
 53F      7    0.1981    0.2004    0.2020    0.0018\
 541     14    0.0986    0.1001    0.1023    0.0010\
 544      7    0.1991    0.2000    0.2008    0.0006\
 553      7    0.1996    0.2000    0.2003    0.0002\
 559      7    0.1998    0.2000    0.2002    0.0001\
 568     14    0.0975    0.1001    0.1036    0.0017\
 572      7    0.1992    0.2001    0.2009    0.0007\
 58B     28    0.0377    0.0500    0.0626    0.0079\
 593      7    0.1999    0.2002    0.2010    0.0004\
 5A6      7    0.1971    0.2007    0.2036    0.0024\
 5CD      7    0.1938    0.1997    0.2061    0.0040

 ### Question 6: Intrusion detection
#### Test case 1:
data = get_data("proj1_data0.csv")
stat = ecu_summary(data, False)
detected, benign = intrusion_detection(data, stat)
print(detected[0])
print(benign[0])
- Output:\
['1597759747.427486', '000', '8', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']
['1597759747.42668', '000', '8', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']

#### Test case 2:
data = get_data("proj1_data0.csv")\
stat = ecu_summary(data, False)\
detected, benign = intrusion_detection(data, stat)\
for i in range(5):\
    print(detected[i])
- Output:\
['1597759747.427486', '000', '8', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']\
['1597759747.428444', '000', '8', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']\
['1597759747.429188', '000', '8', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']\
['1597759747.430111', '000', '8', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']\
['1597759747.430662', '000', '8', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']

#### Test case 3:
data = get_data("proj1_data3_small.csv")\
stat = ecu_summary(data, False)\
detected, benign = intrusion_detection(data, stat)\
print(detected[5])\
print(benign[5])
- Output:\
['1597759356.3397400', '8', '0', '00 00 00 00 00 00 00 00', 'Attack', 'Flooding']\
['1597759356.292780', '8', '130', '08 80 90 80 00 00 07 D3', 'Normal', 'Normal']

### Question 7: Evaluating the intrusion detection system
#### Test case 1:
data = get_data("proj1_data0.csv")\
stat = ecu_summary(data, False)\
detected, benign = intrusion_detection(data, stat)\
result_analysis(data, detected, benign)
- Output:\
Accuracy  :    0.5464\
Precision :    0.0739\
Recall    :    0.9997\
F1 Score  :    0.1376

#### Test case 2:
data = get_data("proj1_data3_small.csv")\
stat = ecu_summary(data, False)\
detected, benign = intrusion_detection(data, stat)\
result_analysis(data, detected, benign)
- Output:\
Accuracy  :    0.6904\
Precision :    0.5142\
Recall    :    0.9994\
F1 Score  :    0.6790

### Question 8: Improving our IDS (only for bonus marks)
- Input:\
upper_sd: 0\
lower_sd: 0\
ceiling: 0

- Output:\
Accuracy  :    0.0902\
Precision :    0.0901\
Recall    :    0.9999\
F1 Score  :    0.1653
