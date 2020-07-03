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

#Greatest Increase
greatest_increase = max(Change_values)
Month_Increase = Month[(Change_values.index(greatest_increase))+1]

#Greatest Decrease
greatest_decrease = min(Change_values)
Month_decrease = Month[(Change_values.index(greatest_decrease))+1]

#Print analysis to terminal
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {Month_Count}")
print(f"Total: ${Total_Revenue}")
print(f" Average Change: ${avg}")
print(f"Greatest Increase in Profits: {Month_Increase} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {Month_decrease} ${greatest_decrease}")