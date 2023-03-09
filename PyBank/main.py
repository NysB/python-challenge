import os
import csv

# Path to collect the file from the Resources folder
csvpath = os.path.join('..','Resources','budget.data.csv')

# Open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read header row 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    #for row in csv_reader:



# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results: