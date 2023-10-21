# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('PyPoll\Resources\election_data.csv')

print("Election Results")
print("----------------------------")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    iTotalVotes = 0
    dict_candidates={}

    # Read each row of data after the header
    for row in csvreader:
        iTotalVotes += 1
        
        if row[2] in dict_candidates.keys():
            dict_candidates[row[2]]+=1
        else:
            dict_candidates[row[2]]=1

print("Total Votes: " + str(iTotalVotes) + "\n")
print("----------------------------\n")

iWinner = 0   
sWinner = ""

for i in dict_candidates:
    print(i + ": " + str(round(dict_candidates[i]*100/iTotalVotes,3)) + "% (" + str(dict_candidates[i]) +")")
    if (iWinner == 0) or (dict_candidates[i] > iWinner):
       iWinner = dict_candidates[i]
       sWinner = i
   
print("\n----------------------------\n")
print(f"Winner: {sWinner}")
print("----------------------------\n\n")

with open('PyPoll\Analysis\output.txt', 'a') as output_file:
    output_file.write('Election Results\n')
    output_file.write('----------------------------\n')
    output_file.write('Total Votes: ' + str(iTotalVotes) + '\n')
    output_file.write('----------------------------\n')
    
    for i in dict_candidates:
       output_file.write(i + ': ' + str(round(dict_candidates[i]*100/iTotalVotes,3)) + '% (' + str(dict_candidates[i]) +')\n')
    
    output_file.write('----------------------------\n')
    output_file.write('Winner: \n')
    output_file.write('----------------------------\n\n')
    