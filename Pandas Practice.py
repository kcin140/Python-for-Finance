#pandas practice
import pandas as pd
from datetime import datetime
import numpy as np

#reading out csv file containing price history for VTSMX
df = pd.read_csv('/Users/Nicholas.Kyburz@ibm.com/Downloads/VTSMX.csv')

#turns df into a datetime manipulatable format
df['datetime'] = pd.to_datetime(df['Date'])
df = df.set_index('datetime')

#specifies only the stock price information where the day of the month == 15
df1 = df[df.index.day == 15]['Adj Close']

#test the final return using the 15th of the month as the day to invest
most_recent = df1[-1]
amount_invested = df1.count() * 100
total = 0
for y in df1:
    total = total + (100/y)
final_value = total * most_recent
final_return = ((final_value - amount_invested)/amount_invested) * 100
print(final_return)

#function that takes in the input and returns the final return in percentage(the value should be the same as the above code output)
def day_of_month(x):
    most_recent = x[-1]
    amount_invested = x.count() * 100
    total = 0
    for y in x:
        total = total + (100/y)
    final_value = total * most_recent
    final_return = ((final_value - amount_invested)/amount_invested) * 100
    print("Total Return: " + str(round(final_return, 2)) + "%")

#an example of running the function with the df1 information
day_of_month(df1)
