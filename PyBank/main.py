#Importing modules
import os
import csv

#Assigning Empty Lists
Month = []
Revenue = []
avg = []
increase = []
decrease = []

#assigning file path
PyBank_data = os.path.join("Resources", "budget_data.csv")

with open(PyBank_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Month Count
        Month.append(row[0])
        Month_Count = len(Month)
        
        #revenue
        Revenue.append(int(row[1]))
        Total_Revenue = sum(Revenue)

    