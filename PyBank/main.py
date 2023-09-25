#Import Modules
import os
import csv

#Create Path
budget_path = os.path.join("Resources", "budget_data.csv")

total_change = []
total_months = []

#Open and read CSV
with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=',')

    #Store header row
    election_header = next(budget_reader)

    #Set counters
    months = 0
    net = 0
    previous_month = 1088983
    variable = 0

    #The total number of months included in the dataset
    for row in budget_reader:
        months += 1
        total_months.append(row[0])

        #The net total amount of "Profit/Losses" over the entire period
        net += int(row[1])

        #The changes in "Profit/Losses" over the entire period
        current_month = row[1]
        change = int(current_month) - int(previous_month)
        previous_month = row[1]
        total_change.append(change)
    #Average those changes
    for x in total_change:
        variable += x
        average_change = round(variable / (months -1), 2)
    #The greatest increase in profits (date and amount) over the entire period
    greatest_change =max(total_change)
    least_change = min(total_change)
    greatest_position = total_change.index(greatest_change)
    least_position  = total_change.index(least_change)
    greatest_date = total_months[greatest_position]
    least_date = total_months[least_position]
  

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net}")
print(f"Average Chage: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_change})")
print(f"Greatest Decrease in Profits: {least_date} (${least_change})")

budget_file = os.path.join("analysis", "budget_file.txt")
with open(budget_file, 'w') as textfile:
    textfile.write("Financial Analysis" + "\n")
    textfile.write("-------------------------------" + "\n")
    textfile.write(f"Total Months: {months}" + "\n")
    textfile.write(f"Total: ${net}" + "\n")
    textfile.write(f"Average Chage: ${average_change}" "\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_change})" "\n")
    textfile.write(f"Greatest Decrease in Profits: {least_date} (${least_change})")
