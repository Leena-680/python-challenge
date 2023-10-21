# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('PyBank\Resources\\budget_data.csv')
output_path = os.path.join('PyBank\Resources\output.csv')

print("Financial Analysis")
print("----------------------------")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    iTotalMonths = 0
    iTotalChange = 0
    iMaxProfit = int(-9999999999)
    iMinProfit = int(9999999999)
    sMaxMonth = ""
    sMinMonth = ""

    # Read each row of data after the header
    for row in csvreader:
        iTotalChange += int(row[1])
        iTotalMonths += 1

        if int(row[1]) > iMaxProfit:
           iMaxProfit = int(row[1])
           sMaxMonth = row[0]

        elif int(row[1]) < iMinProfit:
           iMinProfit = int(row[1])
           sMinMonth = row[0]
        

print(f"Total: {iTotalMonths}")
print(f"Average Change: {iTotalChange}")
print(f"Greatest Increase in Profits: {sMaxMonth} {iMaxProfit}")
print(f"Greatest Decrease in Profits: {sMinMonth} {iMinProfit}")

with open('PyBank\Analysis\output.txt', 'a') as output_file:
    output_file.write('Financial Analysis\n')
    output_file.write('----------------------------\n')
    output_file.write('Total: ' + str(iTotalMonths) + '\n')
    output_file.write('Average Change: ' + str(iTotalChange) + '\n')
    output_file.write('Greatest Increase in Profits: ' + sMaxMonth + ' ' + str(iMaxProfit) + '\n')
    output_file.write('Greatest Decrease in Profits: ' + sMinMonth + ' ' + str(iMinProfit) + '\n')