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
        cashRecords.append([row[0],row[1]])
    
    def find_day_with_highest_increment(cashRecords):
     """Finds the day and amount of the highest increment in Cash-on-Hand.

    Args:
    data: A list of lists, where each inner list contains the day and amount of Cash-on-Hand for a given day.

  Returns:
    A tuple of the day and amount of the highest increment, or None if there are no increments.
  """
    highest_increment = 0
    day_with_highest_increment = None
    for i in range(1, len(cashRecords)):
        current_value = int(cashRecords[i][1])
        previous_value = int(cashRecords[i - 1][1])

        if current_value - previous_value > highest_increment:
         highest_increment = current_value - previous_value
         day_with_highest_increment = cashRecords[i][0]
         cash_on_hand_on_day_with_highest_increment = current_value
        # return day_with_highest_increment, highest_increment

    if day_with_highest_increment is None:
        print("There are no increments in Cash-on-Hand")
    else:
     print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
     print(f"[HIGHEST CASH SURPLUS] DAY:{day_with_highest_increment}, AMOUNT: USD{cash_on_hand_on_day_with_highest_increment}")
#hi nab 
#nablovemark
#hi daris