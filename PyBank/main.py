# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import operator

csvpath = os.path.join('PyBank\Resources\\budget_data.csv')
output_path = os.path.join('PyBank\Resources\output.csv')

print("Financial Analysis")
print("----------------------------")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    iTotalMonths = 0
    iTotalChange = 0   
    iChangeInProfit = 0
    sMonth = ""

    dictChangeInProfit = {}
    listProfit = []

    # Read each row of data after the header
    for row in csvreader:
        
        iChangeInProfit = 0
        if iTotalMonths == 0:
           iLastMonthProfit = int(row[1])
           dictChangeInProfit[row[0]] = iLastMonthProfit
        else: 
           iChangeInProfit = int(row[1]) - iLastMonthProfit
           dictChangeInProfit[row[0]] = iChangeInProfit
           iLastMonthProfit = int(row[1])

        listProfit.append(int(row[1]))
        iTotalChange += int(row[1])
        iTotalMonths += 1

iMaxProfit = int(-9999999999)
iMinProfit = int(9999999999)
sMaxMonth = ""
sMinMonth = ""

sMaxMonth = max(dictChangeInProfit.items(), key=operator.itemgetter(1))[0]
iMaxProfit = dictChangeInProfit.get(sMaxMonth)    

sMinMonth = min(dictChangeInProfit.items(), key=operator.itemgetter(1))[0]
iMinProfit = dictChangeInProfit.get(sMinMonth)  

fAvgProfit = round(float((listProfit[-1] - listProfit[0])/ (iTotalMonths -1)), 2)

print(f"Total Months: {iTotalMonths}")
print(f"Total: ${iTotalChange}")
print(f"Average Change: ${fAvgProfit}")
print(f"Greatest Increase in Profits: {sMaxMonth} ${iMaxProfit}")
print(f"Greatest Decrease in Profits: {sMinMonth} ${iMinProfit}")

with open('PyBank\Analysis\output.txt', 'a') as output_file:
    output_file.write('Financial Analysis\n')
    output_file.write('----------------------------\n')
    output_file.write('Total Months: ' + str(iTotalMonths) + '\n')
    output_file.write('Total: $' + str(iTotalChange) + '\n')
    output_file.write('Average Change: $' + str(fAvgProfit) + '\n')
    output_file.write('Greatest Increase in Profits: ' + sMaxMonth + ' $' + str(iMaxProfit) + '\n')
    output_file.write('Greatest Decrease in Profits: ' + sMinMonth + ' $' + str(iMinProfit) + '\n')