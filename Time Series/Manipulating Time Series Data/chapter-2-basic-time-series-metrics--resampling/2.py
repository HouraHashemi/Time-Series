#------------------------
# Compare Frequency
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
#------------------------

# dwonsampling
dates = pd.date_range(start='2016', periods=4, freq='Q')
data = range(1,5)
quarterly = pd.Series(data=data, index=dates)
print(quarterly)
#------------------------

# upsampleing
monthly = quarterly.asfreq('M')
print(monthly)
#------------------------

# fill missing data, fill methods
monthly = monthly.to_frame('baseline')
# forward fill
monthly['ffill'] = quarterly.asfreq('M', method='ffill')
# backward fill
monthly['bfill'] = quarterly.asfreq('M', method='bfill')
# NaN is 0
monthly['value'] = quarterly.asfreq('M', fill_value='0')

print(monthly)
#------------------------

# reindex()
dates = pd.date_range(start='2016', periods=12, freq='M')
print(dates)
quarterly.reindex(dates)
print(quarterly)

# simple example of reindex

data = {
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}
idx = ["Sally", "Mary", "John", "Monica"]
df = pd.DataFrame(data, index=idx)
print("--------BEFORE--------")
print(df)
newidx = ["Robert", "Cindy", "Chloe", "Pete"]
newdf = df.reindex(newidx)
print("--------AFTER--------")
print(newdf)
