# ML Quarter 1 Project
## Ishan Ajwani and Logan Bradley

Our presentation of the project is in this repository as both a PDF and PPTX.

Our project report is in this repository as a PDF.

This project was mostly done in Weka, and the code is mostly just for initial data cleaning. To do this, first download the data from https://data.montgomerycountymd.gov/Public-Safety/Traffic-Violations/4mse-ku6q/about_data and run **stratified_sample.py** to cut the data down to a usable amount. Next, run **clean_data.py** to make the data usable in Weka. Third, run **description_split.py** to create our new Speeding and Alcohol columns in the data. Finally, run **train_test_split.py** to split into train and test data. The data is now ready for use in Weka.

Inside the Cleaned Data folder are these Python files, as well as .csv files for each intermediate stage of the process.

Finally, the Attribute Selection folder contains .arff files for the train data after each attribute selection method was applied.
