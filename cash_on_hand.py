from pathlib import Path
import csv

# Create a file path to the CSV file
fp = Path.cwd() / "csv" / "cash_on_hand.csv"

#read the csv file to append day and ammount from the csv
with fp.open(mode ="r", encoding = "UTF-8", newline = "") as file:
     reader = csv.reader(file)
     next(reader) #skip header

     #create an empty lists to store day and amount record
     cashRecords=[]

     #append cash on hand into cashrecords lis
     for row in reader:
        cashRecords.append([int(row[0]), int(row[1])])

def compute_difference(cashRecords):
    """Computes the difference in Cash-on-Hand if the current day is lower than the previous day.

    Args:
    data: A list of lists, where each inner list contains the Day and Cash-on-Hand values for a single day.

    Returns:
    A list of tuples, where each tuple contains the Day, Cash-on-Hand, and difference in Cash-on-Hand for a single day.
    """
    difference_in_cash_on_hand = []
    for day in range(len(cashRecords)):
        if day == 0:
            continue
        previous_cash_on_hand = cashRecords[day - 1][1]
        cash_on_hand = cashRecords[day][1]
        if cash_on_hand < previous_cash_on_hand:
            difference = cash_on_hand - previous_cash_on_hand
            difference_in_cash_on_hand.append((cashRecords[day][0], cash_on_hand, difference))
    return difference_in_cash_on_hand

difference_in_cash_on_hand = compute_difference(cashRecords)
for day, cash_on_hand, difference in difference_in_cash_on_hand:
   print(f"Day: {day}, Amount: {cash_on_hand}, Difference: {difference}")










