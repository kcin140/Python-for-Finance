
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
# variables needed are final value of investments, total amount invested, and total return


def end_of_month_DCA(x, start_date, end_date, monthly_contribution):
    panel_data = data.DataReader(x, 'yahoo', start_date, end_date, monthly_contribution)['Adj Close']
    all_end = pd.date_range(start=start_date, end=end_date, freq='BM')
    close = panel_data.reindex(all_end)
    close = close.fillna(method='ffill')
    most_recent = close[-1]
    amount_invested = close.count() * monthly_contribution
    total = 0
    for y in close:
        total = total + (monthly_contribution/y)
    final_value = total * most_recent
    final_return = ((final_value - amount_invested)/amount_invested) * 100
    print("Stock: " + str(x))
    print("Monthly Contribution: $" + str(monthly_contribution))
    print("Start Date: " + str(start_date))
    print("End Date: " + str(end_date))
    print("Total amount invested: $" + str(amount_invested))
    print("Final investment worth: $" + str(round(final_value, 2)))
    print("Total Return: " + str(round(final_return, 2)) + "%")




