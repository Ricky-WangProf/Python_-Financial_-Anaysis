#------------------------Stock Price History Analysis------------------------

import quandl as ql
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
%matplotlib inline

ql.ApiConfig.api_key = 'CeRDHb2M_SEPJx1dsHUC' #API Key

start_date = dt.datetime(2011,1,1) # setup start date
end_date = dt.datetime(2018,1,1)   # setup end date

#------------------------Get historical data from quandl dataset------------------------

GS = ql.get('EOD/HD', start_date=start_date, end_date=end_date)          #Stock Prices history for Goldman Sachs
JPM = ql.get('EOD/JPM', start_date=start_date, end_date=end_date)        #Stock Prices history for JP Morgan Chase
AE = ql.get('EOD/AXP', start_date=start_date, end_date=end_date)         #Stock Prices history for American Express
V = ql.get('EOD/V', start_date=start_date, end_date=end_date)            #Stock Prices history for Visa
CC = ql.get('EOD/KO', start_date=start_date, end_date=end_date)          #Stock Prices history for Coca-Cola
APL = ql.get('EOD/AAPL', start_date=start_date, end_date=end_date)       #Stock Prices history for Apple

tickers = ['GS','JPM','AE','V','CC','APL']                               #ticker list


stock_prices = pd.concat([GS,JPM,AE,V,CC,APL], axis=1, keys=tickers)     # concatenate the dataframe
stock_prices.columns.names = ['Customer Ticker','Stock Info']            

#------------------------Run above cell for initial setup------------------------

stock_prices.head()

#------------------------Run above cell to check head info of concatenated dataframe------------------------


stock_prices.xs(key='Close',axis=1,level='Stock Info').max()

#------------------------Run above cell to check max close price during historical period------------------------

returns = pd.DataFrame()

for tick in tickers:
    returns[tick+' Return'] = stock_prices[tick]['Close'].pct_change()
returns.head()

sns.pairplot(returns[1:])

#------------------------Run above cell to create pairplot to analyze the data------------------------

returns.idxmin()
returns.idxmax()

#------------------------Run above cell to get largest drop and bigest gain date for each stock------------------------

returns.std()

#------------------------Run above cell to get riskest stock during historical period------------------------

sns.distplot(returns.ix['2013-01-01':'2013-12-31']['APL Return'],color='red',bins=100)

#------------------------Run above cell to get distplot of Apple during the year of 2013------------------------

import plotly
import cufflinks as cf
cf.go_offline()

for tick in tickers:
    stock_prices[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

#------------------------Run above cell to get line plot of each stocks during entire period------------------------

sns.clustermap(stock_prices.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

#------------------------Run above cell to create a clustermap of the correlation between the stocks Close Price----

JPM['Close'].ix['2017-01-01':'2018-01-01'].ta_plot(study='boll')

#------------------------Run above cell to create a Bollinger Band Plot for Jp Morgan Chase for 2017----