#------------------------
# Aggregation Methods
#------------------------

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
#------------------------

ozone = pd.read_csv('./air_quality_data/ozone_nyc.csv', parse_dates=['date'], index_col='date')
# print(ozone.info())
# print(ozone.head(3))

ozone = ozone.resample('D').asfreq()
print(ozone.info())
#------------------------

# use mean to aggrigate data
ozone = ozone.resample('M').mean().head()
print(ozone)
# use median to aggrigate data
ozone = ozone.resample('M').median().head()
print(ozone)
# use multiple aggrigation function
ozone = ozone.resample('M').agg(['mean', 'std']).head()
print(ozone)
#------------------------

# ploting data
ozone = pd.read_csv('./air_quality_data/ozone_nyc.csv', parse_dates=['date'], index_col='date')
ozone = ozone.resample('D').asfreq()
print(ozone.info())


ozone = ozone.loc['2016':]
ax = ozone.plot()
monthly = ozone.resample('M').mean()
monthly.add_suffix('_monthly').plot(ax=ax)
plt.show()