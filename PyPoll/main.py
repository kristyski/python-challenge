import os # Modules
import csv

datapath = os.path.join('.', 'Resources', 'election_data.csv') # defines object
outputfile = os.path.join('.', 'analysis', 'output.txt') # output file

with open(datapath) as csvfile: #opens and reads .csv
    reader = csv.reader(csvfile)
    csv_header = next(reader)

    votes = {} # to store all votes in a dictionary
    votecount = 0
    candidates = [] # to store candidates in a list
    
    for row in reader:
        candidate = row[2] #while looking in each row in the candidate column

        if candidate not in candidates: #if candidate is not yet in list candidates
            candidates.append(candidate) #add them to the list
            votes[candidate] = 0 #start their vote count at 0

        votes[candidate] = votes[candidate] + 1 #when found in list, tally how many times in list?
        votecount = votecount + 1  #when found in list add 1 to their vote count

print("Election Results")
print("----------------------")
print(f"Total Votes: {votecount}")
print("----------------------")
for c in candidates:
        print(f'{c}:',
        round(((votes[c] / votecount) * 100),2),'%',
        '(', votes[c],')')
print("----------------------")
winner = max([c]) #well that's not right
print(f"Winner: {winner}")
print("----------------------")

results = (       #tutor showed me, generally, how to do this
        f"\nElection Results\n"
        f"\n----------------------\n"
        f"\nTotal Votes: {votecount}\n"
        f"\n----------------------\n"
        f"\n{c}:{round(((votes[c] / votecount) * 100),2)}% ({votes[c]})\n"
        f"\n----------------------\n"
        f"\nWinner: {winner}\n"
        f"\n----------------------\n"
        )

with open (outputfile, 'w') as txtfile:
    txtfile.write(results)