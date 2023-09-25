#Import Modules
import os
import csv

#Create Path
election_path = os.path.join("Resources", "election_data.csv")

#Set Arrays
candidate_list = []

#Open and read CSV
with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter=',')

    #Store header row
    election_header = next(election_reader)

    #Set counters to 0
    votes = 0
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0

    #Total number of votes cast
    for row in election_reader:
        votes += 1

        #A complete list of candidates who received votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        #The total of votes each candidate won
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        
        if row[2] == "Diana DeGette":
            diana_votes += 1
        
        if row[2] == "Raymon Anthony Doane":
            raymon_votes += 1
        
        #The toal percentage of votes each candidate won
        charles_percentage = round((charles_votes / votes) * 100, 3)
        diana_percentage = round((diana_votes / votes) * 100, 3)
        raymon_percentage = round((raymon_votes / votes) * 100, 3)

        #The winner of the election based on popular vote
        if charles_percentage > diana_percentage and raymon_percentage:
            winner = "Charles Casper Stockham"
        
        elif diana_percentage > charles_percentage and raymon_percentage:
            winner = "Diana DeGette"

        else:
            winner = "Raymon Anthony Doane"


print("Election Results")
print("-------------------------------")
print(f"Total Votes: {votes}")
print("-------------------------------")
print(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})")
print(f"Diana DeGette: {diana_percentage}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

election_file = os.path.join("analysis", "election_file.txt")
with open(election_file, 'w') as textfile:
    textfile.write("Election Results" + "\n")
    textfile.write("-------------------------------" + "\n")
    textfile.write(f"Total Votes: {votes}" + "\n")
    textfile.write("-------------------------------" + "\n")
    textfile.write(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})" + "\n")
    textfile.write(f"Diana DeGette{diana_percentage}% ({diana_votes})" + "\n")
    textfile.write(f"Raymon Anthony Doane{raymon_percentage}% ({raymon_votes})" + "\n")
    textfile.write("-------------------------------" + "\n")
    textfile.write(f"Winner: {winner}" + "\n")
    textfile.write("-------------------------------" + "\n")