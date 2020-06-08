#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries

import numpy as np
import pandas as pd
from pandas_datareader import data, wb
from pandas.testing import assert_frame_equal
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import plotly
import cufflinks as cf
cf.go_offline()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Set Duration

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 1, 1)


# In[3]:


# Import Data using DataReader and set Tickers
# Note: The Tickers are customised here by replacing the Original Tickers to Frequently Used Ticker Names.

BOI = data.DataReader("BIRG.IR",'yahoo',start,end)

SBI = data.DataReader("SBIN.NS",'yahoo',start,end)

AIB = data.DataReader("AIBG.L",'yahoo',start,end)

ICICI = data.DataReader("ICICIBANK.NS",'yahoo',start,end)


# In[4]:


BOI.head()


# In[5]:


SBI.head()


# In[6]:


AIB.head()


# In[7]:


ICICI.head()


# In[8]:


# Display Tickers

tickers = ['BOI','SBI','AIB','ICICI']


# In[9]:


# Concatenate Bank DataFrames together.

bank_stocks = pd.concat([BOI,SBI,AIB,ICICI],axis=1,keys=tickers)


# In[10]:


bank_stocks.head()


# In[11]:


# Set the Column name Levels

bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# In[12]:


bank_stocks.head()


# # Exploratory Data Analysis (EDA)

# In[13]:


# Maximum Close Price

bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()


# In[14]:


returns = pd.DataFrame()


# In[15]:


# Create returns Column for each Bank Stock Ticker

for tick in tickers:
    returns[tick + 'Return'] = bank_stocks[tick]['Close'].pct_change()


# In[16]:


returns.head()


# In[17]:


# Pairplot using Seaborn for returns DataFrame

sns.set()
sns.pairplot(returns[1:])


# In[18]:


# Minimum (or Least) Single Day returns

returns.min()


# In[19]:


# Minimum (or Least) Single Day returns Date display for a single Bank

returns['BOIReturn'].idxmin()


# In[20]:


# Minimum (or Least) Single Day returns Date display for all Banks

returns.idxmin()


# In[21]:


# Maximum (or Most) Single Day returns Date display for all Banks

returns.idxmax()


# In[22]:


# Standard Deviation of the returns

returns.std()


# In[23]:


# Standard Deviation of the returns for a particular year

returns.loc['2018-01-01':'2018-12-31'].std()


# In[24]:


# Distplot using Seaborn for returns of a particular Bank in a particular Year

sns.distplot(returns.loc['2018-01-01':'2018-12-31']['SBIReturn'],color='blue',bins=50)


# In[25]:


# Distplot using Seaborn for returns of a particular Bank in a particular Year

sns.distplot(returns.loc['2018-01-01':'2018-12-31']['AIBReturn'],color='purple',bins=50)


# In[26]:


# Line Plot for Close Price of each bank for entire period

sns.set_style('whitegrid')

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot(figsize=(12,5))


# In[27]:


# iplot for Close Price of each bank for entire period

bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()


# In[28]:


# 30-day Moving Average for Close Price of a particular Bank

plt.figure(figsize=(12,5))
SBI['Close'].loc['2019-01-01':'2020-01-01'].rolling(window=30).mean().plot(label='30 Day Moving Avg.')
SBI['Close'].loc['2019-01-01':'2020-01-01'].plot(label='SBI Close')
plt.legend()


# In[29]:


# Heatmap for Correlation between stocks Close Price

sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# In[30]:


# Clustermap to cluster the Correlations together

sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# In[31]:


# Close Correlation

close_corr = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()


# In[32]:


# Close Correlation using iplot

close_corr.iplot(kind='heatmap',colorscale='rdylbu')


# In[33]:


# Candle Stick Plot using iplot for a particular Banks Stock in a particular Year

sbi17 = SBI[['Open','High','Low','Close']].loc['2017-01-01':'2018-01-01']
sbi17.iplot(kind='candle')


# In[34]:


# SMA plot for a particular Bank in a particular Year

BOI['Close'].loc['2017-01-01':'2018-01-01'].ta_plot(study='sma',periods=[9,18,27])


# In[35]:


ICICI['Close'].loc['2017-01-01':'2018-01-01'].ta_plot(study='sma')


# In[ ]:




