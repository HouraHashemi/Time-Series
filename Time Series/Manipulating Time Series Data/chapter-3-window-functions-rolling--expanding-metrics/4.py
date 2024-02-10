#------------------------
# Relationships between time series: correlation
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
from numpy.random import normal, seed, choice
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns


# cover = sum(xi-x)(yi-y)/sxsy -1,+1

data = pd.read_csv('./stock_data/asset_classes.csv', parse_dates=['Date'],
                   index_col='Date')
print(data.dropna().info())

daily_returns = data.pct_change()
sns.jointplot(data=daily_returns)
plt.show()

# correlation
correlations = daily_returns.corr()
print(correlations)

# heatmap
sns.heatmap(correlations, annot=True)
plt.show()