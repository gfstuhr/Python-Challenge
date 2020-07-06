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

max_votes = Candidates_Votes.index(max(Candidates_Votes))
winner = Candidates[max_votes]

#Print Statements
print("Election Results")
print("-"*30)
print(f"Total Votes: {voter_count}")
for Candidate in range(len(Candidates)):
    print(f"{Candidates[Candidate]}: {Candidates_Percentage[Candidate]}% ({Candidates_Votes[Candidate]})")
print("-"*30)
print(f"The winner is: {winner}!")

#Output text file
output = os.path.join("Poll_Results","Poll_Results.txt")
with open(output,"w") as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("-"*30 + "\n")
    txtfile.write(f"Total Votes: {voter_count} \n")
    for Candidate in range(len(Candidates)):
        txtfile.write(f"{Candidates[Candidate]}: {Candidates_Percentage[Candidate]}% ({Candidates_Votes[Candidate]}) \n")
    txtfile.write("-"*30 + "\n")
    txtfile.write(f"The winner is: {winner}!")