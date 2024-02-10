#------------------------
# Window Function
# Rolling: same size, sliding
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

data = pd.read_csv('./stock_data/google.csv', parse_dates=['Date'], index_col='Date')
print(data.info())
print(data)

# contain days
r90 = data.rolling(window='90D').mean()
data['mean90'] = r90

google = pd.read_csv('./stock_data/google.csv', parse_dates=['Date'], index_col='Date')
google.join(r90.add_suffix('_mean_90')).plot()
plt.show()

r360 = data['Close'].rolling(window='360D').mean()
data['mean90'] = r360
data.plot()
plt.show()


r = data.Close.rolling('90D').agg(['mean', 'std'])
r.plot(subplots=True)
plt.show()