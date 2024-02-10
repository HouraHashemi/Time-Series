#------------------------
# Window Function
# Expanding: contain all prior values
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.DataFrame({'data': range(5)})
df['expanding sum'] = df.data.expanding().sum()
df['cumulative sum'] = df.data.cumsum()
print(df)


data = pd.read_csv('./stock_data/sp500.csv', parse_dates=['date'], index_col='date')

# (rt)running return = (current price/ last price) - 1
# Rt = (1+r1)(1+r2)...(1+rt) - 1
pr = data.SP500.pct_change() #period return
pr_plus_one = pr.add(1)
cumulative_return = pr_plus_one.cumprod().sub(1)
cumulative_return.mul(100).plot()
plt.show()

# max min
data['running_min'] = data.SP500.expanding().min()
data['running_max'] = data.SP500.expanding().max()
data.plot()
plt.show()


def multi_period_return(period_return):
    return np.prod(period_return + 1) - 1
pr = data.SP500.pct_change()
r = pr.rolling('360D').apply(multi_period_return)
data['Rolling  1-year Return'] = r.mul(100)
data.plot(subplots=True)
plt.show()