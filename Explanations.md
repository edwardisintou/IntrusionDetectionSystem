# CITS2401 Project Editorial

## Intrusion Detection System

## Section 1: Data preprocessing
We will perform the data initially to perform intrusion detection.

### Question 1: Import data
The primary objective of Task1 is to collect essential data from the provided dataset. The dataset file, presented in CSV format, along with instructions and a quick preview in Figure 1, will be provided to you (on the Quiz Server). The file contains multiple columns, and you should focus on the essential ones while disregarding the others.\
- Timestamp: The time the data was measured
- Arbitration_ID: Specifies which ECU should receive the data
- Data: The payload (i.e., the command for the ECU to execute)
- Class: Label specifying whether the data is Normal or Attack.

Now, your task is to write a function get_data(filename) that retrieves the data from the given file filename (the file is in CSV format) by returning every entry INCLUDING the headings (the headings always exist in given files, this will be used later for finding indices of columns) as a single list. Each entry should be a list containing data separated by a comma, and any new line characters at the end of each row should be stripped off. It's important to note that no imports should be used for this task.

You may assume there are no errors in the given and tested files.
