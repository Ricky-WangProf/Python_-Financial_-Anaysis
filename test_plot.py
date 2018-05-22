import quandl as ql
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

ql.ApiConfig.api_key = 'CeRDHb2M_SEPJx1dsHUC'
start_date = dt.datetime(2011,1,1)
end_date = dt.datetime(2018,1,1)
GS = ql.get('EOD/HD', start_date=start_date, end_date=end_date)
JPM = ql.get('EOD/JPM', start_date=start_date, end_date=end_date)
tickers = ['GS','JPM']
stock_prices = pd.concat([GS,JPM], axis=1, keys=tickers)
stock_prices.columns.names = ['Bank Ticker','Stock Info']

stock_prices.head()


returns = pd.DataFrame()

for tick in tickers:
    returns[tick+' Return'] = stock_prices[tick]['Close'].pct_change()
returns.head()

pic = sns.pairplot(returns[1:])

plt.show()

