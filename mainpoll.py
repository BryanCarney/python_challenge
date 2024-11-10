# Import necessary modules - used from PyBank starter code
import csv
import os

# Files to load and output

# Input file path
file_to_load = os.path.join("Resources", "election_data.csv")
# Output file path
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables to track the election data
# Track the total number of votes cast
total_votes = 0
# Dictionary to track votes for each candidate 
candidate_votes = {}  

# Decalring the Winning Candidate and Winning Count Tracker - Giraffe Acadamy course explained the use of assignment of "None"
winning_votes = 0
winning_candidate = None

# Opening the CSV file from the variables I assigned above and then allow the code to begin to process it
with open(file_to_load, newline='') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row - same priciple used in PyBank code
    header = next(reader)

    # Created the "For" Loop so the code could through each row of the dataset and then process it
    for row in reader:
# Add on top of the total vote count - same principle used in PyBank code
        total_votes += 1  

# Get the candidate's name from the row and since the candidate name is in the 3rd column, it is directed there. 
        candidate = row[2]

# As I didnt create a list of the candidate names and kept the dictionary "open".  The below code (based of class example) accounts for when candidate is in and not in the dictionary, add them with a starting vote count of 0
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

# Caluclate and add to the candidate's vote count
        candidate_votes[candidate] += 1

# creating the variable in order to calculate the percentages and then to determine the "winning vote recipient"
candidate_percentages = {}
for candidate, votes in candidate_votes.items():

# Calculate the percentage of total votes for this candidate
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

# Based on the above the below code will allow me to see which of the candidates has the most votes - this will be used to assign the winner
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate

# Open the output file and write the results.  Same logic applied from PyBank code
with open(file_to_output, 'w', newline='') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-----------------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes:,}\n")
    txtfile.write(f"-----------------------------------------\n")

# Write each candidate's vote count and percentage.  Help sources from https://docs.python.org/3/library/csv.html to troubleshoot code to write into text file.  Was a licky more tricky than the PyBank example.
    for candidate in candidate_votes:
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]:,})\n")

    txtfile.write(f"-----------------------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write(f"Congratulations, {winning_candidate}!\n")
    txtfile.write(f"-----------------------------------------\n")

# Help sources from chatGPT as the simple logic to use print(file_to_output) did not allow me to display in terminal window
with open(file_to_output, 'r') as txtfile:
    print(txtfile.read())