import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


# The date data type is not time
# Convert to datetime64[ns]
google = pd.read_csv('./stock_data/google.csv')
print(google.info())
print(google)

google.Date = pd.to_datetime(google.Date)
print(google.info())
print(google)


# Convert to index
print("----------------------")
google.set_index('Date', inplace=True)
print(google.info())
print(google)


# Year of 2014
print("----------------------")
print(google['2014'].info())
print(google['2014-1': '2014-5'].info())
print(google.loc['2016-6-1', 'Close'])

print(google.info())
print(google.asfreq('D').info())
print(google.asfreq('B').info()) #business days

print(google[google.Close.isnull()])


# Exercise
print("----------------------")
data = pd.read_csv('./air_quality_data/nyc.csv')
# Inspect data
print(data.info())# Convert the date column to datetime64
data.date = pd.to_datetime(data.date)
# Set date column as index
data.set_index('date', inplace=True)
# Inspect data 
print(data.info())
# Plot data
data.plot(subplots=True)
plt.show()
