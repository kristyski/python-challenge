# open/use csv open and read Modules
import os
import csv

datapath = os.path.join('.', 'Resources', 'budget_data.csv') # defines object
outputfile = os.path.join('.', 'analysis', 'output.txt') # output file

# open file, store in variable called csvfile
with open(datapath) as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)
    
    diff_list = [] # create a list to hold the differences between months
    monthlabel = [] # list to holds month labels
    values = [] # list to holds monthly totals
    previous = 0
    month = 0
    
    for row in reader:
        current = row[1]
        month += 1 # same as month = month + 1
        monthvalue = row[0]
        
        if previous != 0:
            difference = float(current) - float(previous)
            diff_list.append(difference)
            monthlabel.append(monthvalue)
            previous = current
            values.append(float(previous))

        else:
            difference = 0
            monthlabel.append(monthvalue)
            previous = current
            values.append(float(previous))

average = round(sum(diff_list) / len(diff_list),2)
gincrease = max(diff_list)
gdecrease = min(diff_list)


results = ( #can't take credit, tutor showed me how to do this
     f"\nFinancial Analysis\n"
     f"\n--------------------------------\n"
     f"\nTotal Months: {len(values)}\n"
     f"\nTotal: ${sum(values)}\n"
     f"\nNet Total P/L: ${sum(diff_list)}\n"
     f"\nAverage Change: ${average}\n"
     f"\nGreatest Increase in Profits: {monthlabel[(diff_list.index(gincrease)+1)]} $({gincrease}\n"
     f"\nGreatest Decrease in Profits: {monthlabel[diff_list.index(gdecrease)+1]} $({gdecrease})\n"
)

print(f"Financial Analysis")
print("--------------------------------")
print(f"Total Months: {len(values)}")
print(f"Total: ${sum(values)}")
print(f"Net Total P/L: ${sum(diff_list)}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {monthlabel[(diff_list.index(gincrease)+1)]} $({gincrease})")
print(f"Greatest Decrease in Profits: {monthlabel[diff_list.index(gdecrease)+1]} $({gdecrease})")

with open (outputfile, 'w') as txtfile:
    txtfile.write(results)