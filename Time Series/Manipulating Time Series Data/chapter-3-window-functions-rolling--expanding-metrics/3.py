#------------------------
# Creating data
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
from numpy.random import normal, seed, choice
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns


# normal distribution
seed(42)
random_returns = normal(loc=0, scale=0.01, size=1000)
sns.distplot(random_returns, fit=norm, kde=False)
plt.show()

# creating prices
return_series = pd.Series(random_returns)
random_prices = return_series.add(1).cumprod().sub(1)
random_prices.mul(100).plot()
plt.show()
#------------------------

# creating price and return 
data = pd.read_csv('./stock_data/sp500.csv', parse_dates=['date'], index_col='date')
data['returns'] = data.SP500.pct_change()
data.plot(subplots=True)
plt.show()


sns.distplot(data.returns.dropna().mul(100),fit=norm)
plt.show()
#------------------------

# generate random S&P 500 returns
sample = data.returns.dropna()
n_obs = data.returns.count()
random_walk = choice(sample, size=n_obs)
random_walk = pd.Series(random_walk, index=sample.index)
random_walk.head()

start = data.SP500.frist('D')
sp500_random = start.append(random_walk.add(1))
sp500_random.head()
