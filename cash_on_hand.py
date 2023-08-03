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


    def find_days_with_decrease_in_cash_on_hand(cashRecords):
      """Finds the days thwith decreases in Cash-on-Hand.

      Args:
      data: A list of lists, where each inner list contains the day and amount of Cash-on-Hand for a given day.

      Returns:
      A list of days with decreases in Cash-on-Hand, or an empty list if there are no decreases.
      """
      days_with_decrease = []
      for i in range(1, len(cashRecords)):
        current = int(cashRecords[i][1])
        previous = int(cashRecords[i - 1][1])

      if current < previous:
        days_with_decrease.append((cashRecords[i][0], current - previous))
    
      return days_with_decrease
      
    days_with_decrease = find_days_with_decrease_in_cash_on_hand(cashRecords)



    if days_with_decrease:
      print("The days with decreases in Cash-on-Hand are:")
    for day, amount in days_with_decrease:
      print(f"Day {day}: {amount}")
    else:
      print("There are no decreases in Cash-on-Hand")

# print(days_with_decrease)
