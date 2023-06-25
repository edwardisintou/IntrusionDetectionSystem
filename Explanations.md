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
- The headings have the same formatting, other than the number-related ones.\
The function only prints the above output only if to_print is set to True, which is set to True by default.

Finally, return the statistics results as a list, where each data is a tuple containing the ID, Count, Min TS,
Avg TS, Max TS and the SD TS.
#### This concludes section 1 pre-processing, now we can move onto intrusion detection!
