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