import pandas as pd
import numpy as np
from datetime import datetime


# Time Stamp
time_stamp = pd.Timestamp(datetime(2017,1,1))
print(time_stamp)
print(time_stamp.year, time_stamp.month, time_stamp.day, time_stamp.day_name())


#Period
print("----------------------")

period = pd.Period('2022-01', freq='M')
print(period)
print(period.asfreq('D'))

period.to_timestamp().to_period('M')
print(period) 

period = period + 1
print(period)


# Sequence of time stemp
print("----------------------")
index = pd.date_range(start='2017-1-1', periods=12, freq='M')
print(index)
print(type(index[0]))


index = index.to_period()
print(index)
print(type(index[0]))


# Create time series
print("----------------------")
info = pd.DataFrame({'data': index}).info()
print(info)


# According to period datafram
print("----------------------")
periods = pd.period_range('2022-01', '2022-03', freq='M')
data = np.random.rand(len(periods))
print(periods)
print(data)
df = pd.DataFrame(data=data, index=periods, columns=['RandomData'])
print(df)


#Two columns dataframe
print("----------------------")
periods = pd.period_range('2022-01', '2022-12', freq='M')
data = np.random.random((12, 2))  # Corrected line
df = pd.DataFrame(data, index=periods).info()
print(df)

df = pd.DataFrame(data, index=periods, columns=['RandomData1', 'RandomData2'])
print(df)


# Exercise
print("----------------------")

# Create the range of dates here
seven_days = pd.date_range('2017-1-1', periods=7)
# Iterate over the dates and print the number and name of the weekday
for day in seven_days:
    print(day.dayofweek, day.day_name())
