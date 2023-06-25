# CITS 2401 Computer Analysis and Visualisation

## Project 1: Detecting Intrusions in Smart Cars
### 50/50 HD
I was one of students that in Task 8 (bonus question) Hall of the Fame:
- Top Accuracy: Tom Westcott (0.9141)
- Top Precision: Andriko Xanthis (1.0000)
- Top Recall: Edward Le (0.9999)
- Top F1-Score (fastest) : Yinghao Zhang (0.5655)

### Outline
In a world where everything is becoming smarter, have you ever wondered what it truly means for a device to be "smart"? With the Internet of Things (IoT) connecting everything, including our cars, smart vehicles are becoming increasingly popular as they offer advanced features such as streaming audio and video directly from your car and updating firmware on the go. But this also leaves our vehicles vulnerable to cyber-attacks from hackers who can take control of our cars. This is where you come in.

In this project, you will be implementing an Intrusion Detection System (IDS) for smart vars (also referred to as smart vehicles) in Vehicle Networks. There are several approaches to detecting intrusions in smart cars, and one of the simplest but often quite effective methods is through statistical analysis. By identifying outliers in the data, we can detect and alert users to potential security breaches. Throughout this project, we'll be implementing this technique and exploring how it can be used to enhance the security of smart vehicles.

* More details about the questions are provided in file "Explanations".

## Section 1: Data preprocessing

### Question 1: Import data
Write function get_data(filename) to collect data from the provided dataset.

### Question 2: Find unique IDs
Write function unique_id(data) to find a list of unique arbitration IDs.

### Question 3: Retrieve relevant data
Write function ecu_data(arbitration_id, data) that collects data related to the given ID.

### Question 4: Measuring the time intervals
Write function ecu_time_interval(arbitration_id, data) to find the time interval between each data point for the given ID.

### Question 5: Summarising the statistics
Write function ecu_summary(data, to_print) to print a summary in the specific format.

## Section 2: Intrusion detection using statistical analysis

### Question 6: Intrusion detection
Write function intrusion_detection(data, stats, upper_sd, lower_sd, ceiling) to classify each interval as intrusion or non-intrusion

### Question 7: Evaluating the intrusion detection system
Write function result_analysis(data, detected, benign) to print the statistical analysis results of the system.

### Question 8: Improving our IDS (only for bonus marks)
Change the default values of some parameters to improve the system performance.