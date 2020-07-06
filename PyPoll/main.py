#Importing modules
import os
import csv

#Assigning Empty Lists
Candidates = []
voters = []
Candidates_Votes = []
Candidates_Percentage = []

#assigning file path
Pypoll_data = os.path.join("Resources", "election_data.csv")

with open(Pypoll_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Total Votes
        voters.append(row[0])
        voter_count = len(voters)

        #List of Candidates and counting votes
        Candidate = row[2]
        if Candidate not in Candidates:
            Candidates.append(Candidate)
            Candidates_Votes.append(1)
       
        else:
            Candidates_match = Candidates.index(Candidate)
            Candidates_Votes[Candidates_match] = Candidates_Votes[Candidates_match] + 1

#Candidates % and Winner
for Candidate in Candidates_Votes:
    Candidates_Percentage.append(round(((Candidate/voter_count)*100),2))

#Print Statements
print("Election Results")
print("-"*30)
print(f"Total Votes: {voter_count}")
print("-"*30)
print(Candidates)
print(Candidates_Votes)
print(Candidates_Percentage)  