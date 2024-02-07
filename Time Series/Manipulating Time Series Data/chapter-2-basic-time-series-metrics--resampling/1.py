#------------------------
# normalaizing 
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# the date data type is not time
# convert to datetime64[ns]
google = pd.read_csv('./stock_data/google.csv', parse_dates=['Date'], index_col='Date')
print(google.head(3))
print(google)
print(google.loc['2014-01-05', 'Close'])
first_price = google.Close.iloc[0]
print(first_price)


# normalizing
normalized = google.Close.div(first_price).mul(100)
normalized.plot(title="Google Normalized Series")
plt.show()
print(normalized)


#------------------------
# compare more than one price

# yahoo google apple
prices = pd.read_csv('./stock_data/stocks_4.csv', parse_dates=['Date'], index_col='Date')
print(prices.head(1))
normalized = prices.div(prices.iloc[0]).mul(100)
normalized.plot(title="Google - Apple Normalized Series")
plt.show()
print(normalized)


