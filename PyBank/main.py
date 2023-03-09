import csv
import os

# Define path to file and open
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print("Header row:" + str(csv_header))

    # Define variables

    number_months = 0
    total_amount = 0
    change_amount = 0
    current_amount = 1088983
    greatest_increase_month = " "
    greatest_increase_amount = 0
    greatest_decrease_month = " "
    greatest_decrease_amount = 0


    for row in csvreader:

        # The total number of months included in the dataset
        number_months += 1

        # The net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1])

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        change_amount += (int(row[1]) - current_amount)
        
        # The greatest increase in profits (date and amount) over the entire period
        
        if (int(row[1]) - current_amount) > greatest_increase_amount:
            greatest_increase_amount = (int(row[1]) - current_amount)
            greatest_increase_month = row[0]
                
        # The greatest decrease in profits (date and amount) over the entire period
        if (int(row[1]) - current_amount) < greatest_decrease_amount:
            greatest_decrease_amount = (int(row[1]) - current_amount)
            greatest_decrease_month = row[0]
        
        # Set current_amount
        current_amount = int(row[1])

# Your analysis should align with the following results:  

print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(number_months))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(round(change_amount / (number_months-1),2)))
print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase_amount) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease_amount) + ")")