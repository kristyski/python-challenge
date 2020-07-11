## PyPoll

#   The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.
#   Your task is to create a Python script that analyzes the votes and calculates each of the following:
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
import os
import csv

datapath = os.path.join('Resources', 'election_data.csv') # defines object

# open file, store in variable called csvfile
with open(datapath) as csvfile:
    reader = csv.reader(csvfile)

# read header row, this just alerts that a header row exists or is it next(csv_reader, None)
    csv_header = next(reader)

    votes = [] # create a list to hold all votes
#     monthlabel = []
#     values = []
#     previous = 0
#     month = 0

    for row in reader:
        votes.append()

print(f"Total Votes: {len(votes)}")

#         current = row[1]
#         month += 1 # same as month = month + 1
#         monthvalue = row[0]
#         monthlabel.append(monthvalue)
#         values.append(float(previous))
        
#         if previous != 0:
#             difference = float(current) - float(previous)
#             diff_list.append(difference)
            
#             # monthlabel.append(monthvalue)
#             # values.append(float(previous))

#             previous = current

#         else:
#             difference = 0
#             diff_list.append(difference)
              # monthlabel.append(monthvalue)
              # values.append(float(previous))
#             previous = current

# average = round(sum(diff_list) // (len(diff_list)-1),3)
# print (average)
# #print (diff_list)
# #print (monthlabel)
# #print (values)
# print(f"Total Value: $ {sum(values)}")
# print(f"Net Total P/L: ${sum(diff_list)}")
# print(f"Average Change: ${average}")