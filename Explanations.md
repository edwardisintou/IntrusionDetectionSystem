# CITS2401 Project Editorial

## Intrusion Detection System

## Section 1: Data preprocessing
We will perform the data initially to perform intrusion detection.

### Question 1: Import data
The primary objective of Task1 is to collect essential data from the provided dataset. The dataset file, presented in CSV format, along with instructions and a quick preview in Figure 1, will be provided to you (on the Quiz Server). The file contains multiple columns, and you should focus on the essential ones while disregarding the others.
- Timestamp: The time the data was measured
- Arbitration_ID: Specifies which ECU should receive the data
- Data: The payload (i.e., the command for the ECU to execute)
- Class: Label specifying whether the data is Normal or Attack.

Now, your task is to write a function get_data(filename) that retrieves the data from the given file filename (the file is in CSV format) by returning every entry INCLUDING the headings (the headings always exist in given files, this will be used later for finding indices of columns) as a single list. Each entry should be a list containing data separated by a comma, and any new line characters at the end of each row should be stripped off. It's important to note that no imports should be used for this task.

You may assume there are no errors in the given and tested files.

### Question 2: Find unique IDs
For this task, you need to implement a function called unique_id(data) which takes in the data as a list of lists and returns a list of unique arbitration IDs. The IDs are in the form of a string and are stored in a hexadecimal format. The returned list of IDs should be sorted in ascending order based on their string value. That is, you don't need to convert the type of the IDs into any other data type, as sorting by their default data type (string) is expected.

Please note that, the order of columns in the provided CSV file may differ from file to file, so you should not assume that the column you are interested in will always be in the same position. You should use the header row (the first row in the CSV file) to identify the correct column based on its name, rather than its position in the file.

### Question 3: Retrieve relevant data
In this task, you are to write a function ecu_data(arbitration_id, data) that collects the timestamp and data associated with the given arbitration_ID and returns the list. Remember, this list does NOT contain the heading row. Only the rows in data that match the arbitration_ID are saved (where each row is also a list). The order of the columns may vary between files, but this order should not be modified. Hence, the final list returned is a nested list.


### Question 4: Measuring the time intervals
The next thing we need to do is to measure the time interval for each ECU (identified by the arbitration ID). In this task, you need to write a function ecu_time_interval(arbitration_id, data) that returns the list that contains the time interval between each data point for the chosen arbitration ID in the dataset. Here, data is the data retrieved from Task 1. Ensure to convert data types as appropriate. Since the columns may vary between datasets, the index of the timestamp column must be checked. An example is shown in Figure 4 using the data shown in Figure 3. As we are calculating the time differences, the size of the returning list will be one less than the size of the data for the chosen arbitration_ID.

Hint, you are expected to utilise some of the previously implemented functions to complete this task.

### Question 5: Summarising the statistics
Your task is to write a function ecu_summary(data, to_print) that should output a summary in the format specified below:
- ID: is the arbitration ID found in the data.
- Count: is the number of times the given arbitration ID appears in the data.
- Min TS: is the minimum time interval value for the given arbitration ID.
- Avg TS: is the average time interval value for the given arbitration ID.
- Max TS: is the maximum time interval value for the given arbitration ID.
- SD TS: is the standard deviation of the time interval values for the given arbitration ID.

Apply the formatting as follows:
- All values are right aligned, including the headings.
- ID has a default width of 4 characters.
- Count has a default width of 7 characters.
- Min TS has a default width of 10 characters and is formatted to 4 decimal places.
- Avg TS, Max TS and SD TS are formatted the same as the Min TS.
- The headings have the same formatting, other than the number-related ones.

The function only prints the above output only if to_print is set to True, which is set to True by default.

Finally, return the statistics results as a list, where each data is a tuple containing the ID, Count, Min TS, Avg TS, Max TS and the SD TS.
#### This concludes section 1 pre-processing, now we can move onto intrusion detection!

## Section 2: Intrusion detection using statistical analysis
We can use statistical analysis as a simple method to detect intrusions in this case. The approach involves identifying outliers based on the statistical analysis we performed in section 1. For example, if the time interval between the ECU data points is significantly slower or faster, then it could be regarded as an intrusion. We will now proceed to implement this method.

### Question 6: Intrusion detection
* This part is the most complex one in this project, so please make sure to read it carefully.

You will write a function intrusion_detection(data, stats, upper_sd, lower_sd, ceiling) that returns two lists – detected and benign.

The input parameters:
- data: This is the list retrieved from the get_data function.
- stats: This is the list retrieved from the ecu_summary function.
- upper_sd: This is the upper SD value we will use for filtering outliers (i.e., intrusions). The default value is set to 3.
- lower_sd: This is the lower SD value we will use for filtering outliers (i.e., intrusions). The default value is set to 3.
- ceiling: This is how frequently we are detecting intrusions, which rounds the time interval values. The default value is set to 0.01 (i.e., every 10ms).

To detect intrusions based on statistical analysis, you can use the mean and standard deviation (SD) values calculated from the data. This is done for EACH Arbitration_ID data. To determine the upper and lower boundaries, you need to multiply the SD value by lower_sd to get the lower boundary and by upper_sd to get the upper boundary. For instance, if the mean was 5 seconds and SD of 1, using the default values for upper_sd and lower_sd (i.e., 3), any time intervals outside the range [2, 8] seconds are considered as intrusions.

Another important value is ceiling, which is the interval that the intrusion detection actually happens. Continuous monitoring can be computationally expensive, so in practice, we take samples at every regular, say x, intervals (here, default is 10ms). But, for this task, the time_interval_ceiling function is already provided to you (see the info of the project on the quiz server before Task 6 question), so you need to use this function to convert the time intervals obtained from the ecu_time_interval function you wrote previously (this is also a hint). Keep in mind that the size of the time interval list is one less than the size of the data list!

From above, you end up with two types of outputs – ones that are classified as intrusion (we will denote these as detected), and ones that are classified as not intrusion (we will denote these as benign). So, you should create two lists to keep track of these two types of outputs and save their relevant data. Here is an example list of ECU data shown in Figure 3. You should be able to see such data using the ecu_data function. The first 10 timestamps for the same arbitration_ID data (i.e., 153) is shown in Figure 4. Please note that the first entry in Figure 4 is the time difference between row 1 and row 2 in Figure 3, and so forth.

For the given data with arbitration ID 153, the Average TS is 0.0097 and the SD TS is 0.0014. If we set upper_sd and lower_sd to be 3 (the default value), then the range becomes [0.0055, 0.0139]. So, any time interval falling outside this range will be regarded as intrusion for ID 153 (for the cases in Figure 4, none of them are regarded as intrusions).

Finally, the function will return two lists – detected and benign. The list detected contains all the data associated with time intervals being outside the detection range. For example, if row 1 in Figure 4 was an intrusion, then row 2 from Figure 3 will be added to the detected list. Any other values not inside the detected list should be placed in the benign list. That is, the size of data – 1 should be equal to the size of detected + benign (the minus 1 is the heading).

### Question 7: Evaluating the intrusion detection system
Our final task is to evaluate how well our intrusion detection system works. This is done by calculating some performance metrics. For our evaluation, we will calculate four metrics – accuracy, precision, recall and F1 score. The calculations of these metrics are all available from this page (you can do your own research in addition to reading this):\
https://en.wikipedia.org/wiki/F-score
- The accuracy measures how well the intrusion detection system has performed.
- The precision measures the ratio of intrusions detected out of all detections.
- The recall measures the ratio of intrusions detected out of all intrusions.
- F1 score measure is a balanced representation of both precision and recall.

For example, high precision means you were able to detect a high number of intrusions. On the other hand, high recall means you have a low number of wrongly classified benign data. In case of high precision and low recall, it means you have likely just labelled most data as intrusion (thus, many false negatives). In case of low precision and high recall, it means many intrusions bypassed the intrusion detection system. So, a good balance between the two are essential in practice, which is measured by F1 Score metric.

You already have two lists – detected and benign, from Task 6. So you can use these two lists to
calculate these metrics.

Write a function result_analysis(data, detected, benign) that prints the statistical analysis results for your intrusion detection system. The outputs should be, in the order:
- Accuracy: label “Accuracy” with the text width being 10, followed by colon “:”, followed by
the result formatted to 4 decimal places with the text width being 10 also.
- Precision, Recall and F1 Score are printed in this order with the same formatting.

Using the default values (i.e., upper_sd and lower_sd set to 3, ceiling set to 0.01) with the dataset proj1_data0.csv, you should get the following output:
- Accuracy: 0.5464
- Precision: 0.0739
- Recall: 0.9997
- F1 Score: 0.1376

In fact, the result is pretty bad! - The F1 Score of 0.1 is actually worse than a random guess (e.g., a coin-flip method will achieve 0.5 F1 Score)! Well thankfully, we can improve our IDS!

### Question 8: Improving our IDS (only for bonus marks)
The base parameter is very bad for our IDS, as its performance metrics are all below average at best. There are three default values we have set, but not really changed in our testings. To improve its performance, we will experiment with changing the default values of some parameters. So let’s change some to see what happens!

A random guess is to increase the upper_sd and lower_sd values. Trying 4 for both gives us:
- Accuracy: 0.5503
- Precision: 0.0745
- Recall: 0.9997
- F1 Score: 0.1387

Not bad, we improved both accuracy and F1 score a little, but we can probably do better. This time, let’s try to decrease the ceiling value (i.e., we take samples faster). Setting ceiling to 0.005 gives us:
- Accuracy: 0.5715
- Precision: 0.0779
- Recall: 0.9997
- F1 Score: 0.1445

Great! So we see that we can increase the performance by altering the parameter values. This should give you some idea that you can fiddle with those three parameters in order to improve your IDS. So now it is your turn to go fiddle with those parameters to get the best results!

Final remarks: make sure you have the module docstring for your project code, indicating your name, your student ID number along with the description of the project.

### Bonus marks
If you participate in Task 8, you can upload your parameter values and the results on the Quiz Server “Project 1 Task 8 submissions” as feedback. You will also be able to check other people’s results on the analysis tab.

Top accuracy or precision or recall or F1 score (total 4 students but doesn’t stack i.e., if you get top in both recall and F1 score, you only get the bonus mark once) – 10 bonus marks.\
Top 20 students for F1 score – 5 bonus marks.\
Top 50 students for F1 score – 2 bonus marks.

- NOTE1: the dataset for testing for this should be proj1_data1.csv!
- NOTE2: If there are two or more submissions with the same parameter values, the first one is counted.
- NOTE3: If you find wrong results for the parameter values submitted, please report them!