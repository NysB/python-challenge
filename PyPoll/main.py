import csv
import os

# Define path to file and open
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    

    # Define variables

    total_votes = 0
    initial_participant_one = " "
    participant_one = " "
    initial_participant_two = " "
    participant_two = " "
    initial_participant_three = " "
    participant_three = " "
    votes_participant_one = 0
    votes_participant_two = 0
    votes_participant_three = 0
    winner = " "

    for row in csvreader:

        # The total number of votes cast

        total_votes += 1

        # A complete list of candidates who received votes

        
        if row[2] != participant_one and row[2] != participant_two and row[2] != participant_three:
            if participant_one != initial_participant_one:
                if participant_two != initial_participant_two:
                    if participant_three != initial_participant_three:
                        print("There are more than 3 participants")
                    else:
                        participant_three = row[2]
                else:
                    participant_two = row[2]
            else:
                participant_one = row[2]
        
        # The total number of votes each candidate won

        if row[2] == participant_one:
            votes_participant_one += 1
        if row[2] == participant_two:
            votes_participant_two += 1
        if row[2] == participant_three:
            votes_participant_three += 1


# The winner of the election based on popular vote

if votes_participant_one > votes_participant_two and votes_participant_one > votes_participant_three:
    winner = participant_one
elif votes_participant_two > votes_participant_one and votes_participant_two > votes_participant_three:
    winner = participant_two
else:
    winner = participant_three


# Your analysis should align with the following results:
print("Election Results")
print("----------------------")
print("Total Votes: " + str(total_votes))
print("----------------------")
print(participant_one + ": " + str(round((votes_participant_one/total_votes)*100,3)) + "% (" + str(votes_participant_one) + ")")
print(participant_two + ": " + str(round((votes_participant_two/total_votes)*100,3)) + "% (" + str(votes_participant_two) + ")")
print(participant_three + ": " + str(round((votes_participant_three/total_votes)*100,3)) + "% (" + str(votes_participant_three) + ")")
print("----------------------")
print("Winner: " + winner)
print("----------------------")


# Specify the file to write to
output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])