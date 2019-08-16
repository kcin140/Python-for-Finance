
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
# variables needed are final value of investments, total amount invested, and total return

#end_of_month_DCA takes in 4 variables: a stock ticker(x), a start and end date and finally a monthly contribution amount invested into this stock
#it will evaluate these inputs by pulling stock data from a yahoo API
# the variable 'all_end' denotes the date range frequency of the calculator- 'BM' means the monthly contribution will buy stock on the last trading day of each month during the time period
#the result of the function will give us: the return on investment(%), the total amount invested, and the final amount that invested would be worth
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



start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
end_of_month_DCA('IBM', start, end, 100 )

