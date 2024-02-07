#------------------------
# Transformation Methods, resemple-interpolate
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
#------------------------

unrate = pd.read_csv('./stock_data/unrate.csv', parse_dates=['Date'], index_col='Date')
print(unrate.info())
print(unrate.head())

# returning new object
unrate.asfreq('MS').info()
unrate.resample('MS')


answer = unrate.asfreq('MS').equals(unrate.resample('MS').asfreq)
print(answer)

#------------------------
# simple example
# create a time series DataFrame
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
data = {'value': range(1, 11)}
df = pd.DataFrame(data, index=date_range)

# downsample to weekly frequency, taking the mean of values
weekly_data = df.resample('W').mean()
print(weekly_data)

# upsample to hourly frequency, using linear interpolation
hourly_data = df.resample('H').interpolate(method='linear')
print(hourly_data)
# print(df)
