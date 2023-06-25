"""
CITS 2401 Computer Analysis and Visualisation
Project 1 2023: Detecting Intrusions in Smart Cars
Author: Edward Le
Student ID: 23020568
In this project, I will be implementing an Intrusion Detection System (IDS) for smart vars (also referred to as smart vehicles) in Vehicle Networks.
By identifying outliers in the data, we can detect and alert users to potential security breaches.
Throughout this project, we will explore how the above technique can be used to enhance the security of smart vehicles.
"""

import statistics
import math

"""Question 1: Import data"""
def get_data(filename):
    """this function gets a filename
    and retrieves the data from the given file"""
    with open(filename, 'r') as filein:
        file_lines = filein.readlines()
    
    line_list = []
    for line in file_lines:
        line_list.append(line.strip().split(","))
        
    return line_list

"""Question 2: Find unique IDs"""
def unique_id(data):
    """this function returns the list of
    sorted unique arbitration IDs from the given data"""
    header = data[0]
    data = data[1:]
    
    index_id = 0
    id_list = []
    
    #check index for id incase it change the spot
    for i in range(len(header)):
        if(header[i].lower() == "arbitration_id"):
            index_id = i
    
    for line in data:
        a_id = str(line[index_id])
        id_list.append(a_id)
    
    unique_id_list = list(set(id_list))
    unique_id_list = sorted(unique_id_list)
    
    return unique_id_list

"""Question 3: Retrieve relevant data"""
def ecu_data(arbitration_id, data):
    """this function  collects the timestamp and data
    associated with the given arbitration_ID and return the list"""
    header = data[0]
    data = data[1:]
    
    index_id = 0
    data_list = []
    
    for i in range(len(header)):
        if(header[i].lower() == "arbitration_id"):
            index_id = i
    
    for line in data:
        if(arbitration_id.lower() == line[index_id].lower()):
            data_list.append(line)
    
    return data_list

"""Question 4: Measuring the time intervals"""
def ecu_time_interval(arbitration_id, data):
    """this function returns the list
    that contains the time interval between each data point
    for the chosen arbitration ID in the dataset. """
    header = data[0]
    data = data[1:]
    
    index_id = 0
    index_time = 0
    
    time_list = []
    time_interval = []
    
    for i in range(len(header)):
        if(header[i].lower() == "arbitration_id"):
            index_id = i
        if(header[i].lower() == "timestamp"):
            index_time = i
    
    for line in data:
        if(arbitration_id.lower() == line[index_id].lower()):
            time_list.append(line[index_time])
            
    #time_difference between 2 time
    for i in range(len(time_list)-1):
        time = abs(float(time_list[i]) - float(time_list[i+1]))
        time_interval.append(time)
    
    return time_interval

"""Question 5: Summarising the statistics"""
def ecu_summary(data, to_print=True):
    """this function summaries the file and then return 
    statistics results as a list, where each data is a tuple""" 
    unique_id_list = unique_id(data)
    
    header = data[0]
    index_id = 0
    
    #id_list is a list of all id
    #small_id_list is a list of all id with same id
    #big_id_list appends small_id_list
    id_list = []
    small_id_list = []
    big_id_list = []    
    big_time_list = []
    
    lst_of_tup = []
    my_lst = [["ID", "Count", "Min TS", "Avg TS", "Max TS", "SD TS"]]
    
    for i in range(len(header)):
        if(header[i].lower() == "arbitration_id"):
            index_id = i
            
    for line in data:
        a_id = line[index_id]
        id_list.append(a_id)
    
    #put lists of time_interval with the same id in 1 big list
    #put lists of same id in 1 big list with same index of time
    for i in range(len(unique_id_list)):
        big_time_list.append(ecu_time_interval(unique_id_list[i], data))
        for j in range(len(id_list)):
            if(id_list[j].lower() == unique_id_list[i].lower()):
                a_id = id_list[j]
                small_id_list.append(a_id)
        big_id_list.append(small_id_list)
        small_id_list = [] #recreate new list with same id
        
        id_value = big_id_list[i][0]
        count_value = len(big_id_list[i])
        min_value = min(big_time_list[i])
        avg_value = finding_average(big_time_list[i]) #find average value using below function
        max_value = max(big_time_list[i])
        sd_value = statistics.stdev(big_time_list[i]) #find standard deviation using statistics
        tup = (id_value, count_value, min_value, avg_value, max_value, sd_value) #tuple for each value of id
        lst_of_tup.append(tup)
        #round values to 4 decimal places using f-string
        my_lst.append([id_value, count_value, f'{min_value:.4f}', f'{avg_value:.4f}', f'{max_value:.4f}', f'{sd_value:.4f}'])
    
    if(to_print): #print if to_print is set to 'True' (which is by default)
        print_format(my_lst) #use function for easier formatting
    return lst_of_tup

def finding_average(lst):
    """this function finds average value of a list"""
    value = sum(lst) / len(lst)
    return value

def print_format(lst):
    """this function formats value to print for task 5"""
    for item in lst:
        print('{:>4} {:>6} {:>9} {:>9} {:>9} {:>9}'.format(*item))
        
def time_interval_ceiling(interval, ceiling=0.01) -> list:
    """given the ceiling value, convert the intervals to the nearest ceiling gap
        this is already provided to the students.
    """
    return [math.floor(row / ceiling) * ceiling for row in interval]

"""Question 6: Intrusion detection"""
def intrusion_detection(data, stats, upper_sd=3, lower_sd=3, ceiling=0.01):
    """this function returns 2 lists: detected and benign
    detected: intrusion
    benign: non intrusion"""
    unique_id_list = unique_id(data)
    
    interval_list = []
    big_data_list = []
    
    lower_list = []
    upper_list = []

    for i in range(len(unique_id_list)):
        #convert time intervals for each unique id using given function
        interval = ecu_time_interval(unique_id_list[i], data)
        interval_list.append(time_interval_ceiling(interval))
        #big_data_list includes all data list of each id to later return
        big_data_list.append(ecu_data(unique_id_list[i], data))
        
        #stats[i][3] is average and stats[5] is standard deviation timestamp of each unique id
        #index 3 and 5 can be used here because they are fixed as part of task 5
        #lower_list and upper_list consist all lower and upper boundary
        #lower boundary is calculated by average - (standard deviation * lower_sd)
        #upper boundary is calculated similarly
        lower_list.append(stats[i][3] - (stats[i][5] * lower_sd))
        upper_list.append(stats[i][3] + (stats[i][5] * upper_sd))
    
    detected_list = []
    benign_list = []
    
    for i in range(len(interval_list)):
        #first row is always considered not intrusion
        benign_list.append(big_data_list[i][0])
        for j in range(len(interval_list[i])):
            #loop in every small data list with same id
            if(interval_list[i][j] < lower_list[i] or interval_list[i][j] > upper_list[i]):
                #starting from second row to the end
                detected_list.append(big_data_list[i][j+1])
            else:
                benign_list.append(big_data_list[i][j+1])
    
    return detected_list, benign_list

"""Question 7: Evaluating the intrusion detection system"""
def result_analysis(data, detected, benign):
    """this function analysises the result to evaluate
    how well our intrusion detection system works"""
    header = data[0]
    index_class = 0
    
    true_positives = 0
    true_negatives = 0
    false_negatives = 0
    
    for i in range(len(header)):
        if(header[i].lower() == "class"):
            index_class = i
    
    #true positives is a value of true detection in detected
    for i in range(len(detected)):
        if(detected[i][index_class].lower() == "attack"):
            true_positives += 1
            
    for i in range(len(benign)):
        #true negatives is a value of correct labeling non intrusion in benign
        if(benign[i][index_class].lower() == "normal"):
            true_negatives += 1
        #false_negatives is a value of incorrect labeling non intrusion in benign
        else:
            false_negatives += 1
    
    #accuracy is calculated using sum of 2 true values devided 2 labels
    #precision is calculated using true positives devided positive lable
    accuracy = (true_positives + true_negatives) / (len(detected) + len(benign))
    precision = true_positives / len(detected)
    recall = true_positives / (true_positives + false_negatives)
    f1 = (2 * precision * recall) / (precision + recall)

    #use format function to print for each value
    print_format2('Accuracy', accuracy) 
    print_format2('Precision', precision)
    print_format2('Recall', recall)
    print_format2('F1 Score', f1)
    
def print_format2(word, value):
    """this function formats to print for task 7"""
    print(f"{word:<10}: {value:>9.4f}")

    data = get_data("proj1_data0.csv")
    interval = ecu_time_interval('153', data)
    for i in range(10):
        print(round(interval[i], 5))