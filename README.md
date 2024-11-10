

# python_challenge PyBank
    Unable to push to github as this was not covered in class yet due to technical issues with Git, so files were uploaded manually 

# Dependencies
    import csv
    import os

# The below came with the original python starter file.  Giving a helping hand to start the project


# Files to load and output (update with correct file paths)
    file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
    file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
    total_months = 0
    total_net = 0


# chose my vaiables to add 2 lists and initially setting my increase and descrease at 0
# Add more variables to track other necessary financial data 
    profit_loss = []
    profit_loss_change = []
    greatest_inc = 0
    greatest_dec = 0


# Provided as part of the original code
# Open and read the csv file
    with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

# Skip the header row
    header = next(reader)

# Extract first row to avoid appending to net_change_list
    first_row = next(reader)


# Allowing my code to begin after the header row and injesting the data to beging the calculations
# Track the total and net change - the following part of code was based on principles from a youtube course offered by Giraffe Acadamy
    total_months += 1
    total_net += int(first_row[1])
    prev_profit_loss = int(first_row[1])

# Process each row of data
    for row in reader:
        total_months += 1
        total_net += int(row[1])
# Track total amount
        start_profit_loss = int(row[1])
# declare the change in position of the data
        change_pos_data = start_profit_loss - prev_profit_loss

# Track the net change, using append to account for the change, "append" utilization also sourced from Giraffe Acadamy course
        profit_loss_change.append(change_pos_data)

# Calculate the greatest increase in profits (month and amount)
        if change_pos_data > greatest_inc:
            greatest_inc = change_pos_data
            greatest_inc_month = row[0]

# Calculate the greatest decrease in losses (month and amount) 
        if change_pos_data < greatest_dec:
            greatest_dec = change_pos_data
            greatest_dec_month = row[0]

        prev_profit_loss = start_profit_loss

# Calculate the average net change across the months - ChatGPT assistance 
    average_change = sum(profit_loss_change) / len(profit_loss_change) if profit_loss_change else 0
# Generate the output summary - using \n to format each action into a new line.
# Add formatting to include commas and decimals so numbers are more readable - help from https://realpython.com/python-f-strings/
    final_summary_data = (
    f"Financial Analysis\n" 
    f"----------------------------\n" 
    f"Total Months: {total_months}\n"
    f"Total: ${total_net:,.2f}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc:,.2f})\n"
    f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec:,.2f})\n"
    )

# Output the analysis to the external text file for submission
    with open(file_to_output, "w") as output_file:
    output_file.write(final_summary_data)

# print so it can be effectively displayed in the Terminal window
    print(final_summary_data)


# **********************python_challenge PyBank********************** 
