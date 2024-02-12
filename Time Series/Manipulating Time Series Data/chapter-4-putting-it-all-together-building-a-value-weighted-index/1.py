
#------------------------
# Market value - weighted index
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
from numpy.random import normal, seed, choice
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns


# share price * number => market value
nyse = pd.read_excel('./stock_data/listings.xlsx', sheet_name='nyse', na_values='n/a')
print(nyse.info())

nyse.set_index('Stock Symbol', inplace=True)
nyse.dropna(subset='Sector', inplace=True)
nyse['Market Capitalization'] /= 1e6 #in million USD
print(nyse.head())

# capitlization
components = nyse.groupby(['Sector'])['Market Capitalization'].nlargest(1)
components.sort_values(ascending=False)
print(components)

tickers = components.index.get_level_values('Stock Symbol')
print(tickers)


columns = ['Company Name', 'Market Capitalization', 'Last Sale']
component_info = nyse.loc[tickers, columns]
print(component_info)