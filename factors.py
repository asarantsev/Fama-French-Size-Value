import numpy as np
import pandas as pd
from verification import plots
from statsmodels.api import OLS

DF = pd.read_excel('factors.xlsx')
size = DF['SMB'].values
value = DF['HML'].values[1:]
vol = DF['Volatility'].values[1:]
rate = DF['Rates'].values
spread = DF['Spreads'].values

Reg = OLS(np.diff(size), pd.DataFrame({'const' : 1, 'vol' : vol, 'lag' : size[:-1], 'rate' : rate[:-1], 'spread' : spread[:-1]})).fit()
print(Reg.summary())
res = Reg.resid
plots(res, 'size')

# Reg = OLS(np.diff(value), pd.DataFrame({'const' : 1, 'lag' : value[:-1]})).fit()
# print(Reg.summary())
# res = Reg.resid
# plots(res, 'value')

