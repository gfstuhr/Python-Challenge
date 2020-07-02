#Importing modules
import os
import csv

#Assigning Empty Lists
Month = []
Revenue = []
Change_values = []

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

        #finding change values
    for i in range(len(Revenue)-1):
        change = int(Revenue[i+1]) - int(Revenue[i])
        Change_values.append(change)
    
    #average change
    avg = round(sum(Change_values)/len(Change_values),2)

print(Month_Count)
print(Total_Revenue)
print(avg)
    
    