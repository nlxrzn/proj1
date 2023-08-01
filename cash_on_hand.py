from pathlib import Path
import csv

#create a file to csv file
fp = Path.cwd()/"csv"/"cash_on_hand.csv"

#read the csv file to append day and ammount from the csv
with fp.open(mode ="r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader) #skip header

    #create an empty lists to store day and amount record
    cashRecords=[]

    #append cash on hand into cashrecords lis
    for row in reader:
        cashRecords.append([row[0],row[2]])

