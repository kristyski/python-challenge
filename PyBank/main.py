# The dataset is composed of two columns: `Date` and `Profit/Losses`

# open/use csv open and read Modules
import os
import csv

datapath = os.path.join('.', 'Resources', 'budget_data.csv') # defines object

# open file, store in variable called csvfile
with open(datapath) as csvfile:
    reader = csv.reader(csvfile)
   # next(csvfile)

# read header row, this just alerts that a header row exists or is it next(csv_reader, None)
    csv_header = next(reader)

# The net total amount of "Profit/Losses" over the entire period:

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
            diff_list.append(difference)
            monthlabel.append(monthvalue)
            previous = current
            values.append(float(previous))

#print (diff_list) # this is just to check what's in the list, delete when done
average = round(sum(diff_list) / len(diff_list),2)
gincrease = max(diff_list)
gdecrease = min(diff_list)

# print(diff_list.index(gincrease))
# print(monthlabel[25])
# print(diff_list.index(gdecrease))
# print(monthlabel[44])
print(f"Total Months: {len(diff_list)}")
print(f"Total: ${sum(values)}")
print(f"Net Total P/L: ${sum(diff_list)}")
print(f"Average Change: ${average}  THIS IS DIVIDING BY 85 not 86")
print(f"Greatest Increase in Profits: {monthlabel[25]} $({gincrease})")
print(f"Greatest Decrease in Profits: {monthlabel[44]} $({gdecrease})")