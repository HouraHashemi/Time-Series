#------------------------
# moving data accrous the time
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# the date data type is not time
# convert to datetime64[ns]
google = pd.read_csv('./stock_data/google.csv', parse_dates=['Date'], index_col='Date')
print(google.info())
print(google)


# one period to the future to comapre data
google['shifted'] = google.Close.shift(periods=1)
print(google)

google['lagged'] = google.Close.shift(periods=-1)
print(google)


# percent change xt / xt - 1 | financial return
# each cloumn value of change would be Close/shifted
# simple example:
# data = {
#   "points": [100, 120, 114],
#   "total": [350, 340, 402]
# }
# df = pd.DataFrame(data)
# print(df.div(10))
# output:
#    points  total
# 0    10.0   35.0
# 1    12.0   34.0
# 2    11.4   40.2


google['change'] = google.Close.div(google.shifted)
print(google)

# reletive change in percentage of prices
# simple example:
# data = {
#   "points": [100, 120, 114],
#   "total": [350, 340, 402]
# }
# df = pd.DataFrame(data)
# df['return']  = df.total.sub(1).mul(100)
# print(df)
# output
#    points  total  return
# 0     100    350   34900
# 1     120    340   33900
# 2     114    402   40100


google['return'] = google.change.sub(1).mul(100)
print(google)

# diff x - (x-1) last time stock trated
google['diff'] = google.Close.diff()
print(google)


google['easy_method_of_return'] = google.Close.pct_change(periods=1).mul(100)

print(google[['Close', 'shifted', 'lagged', 'change', 'return', 'diff', 'easy_method_of_return']].head(5))
