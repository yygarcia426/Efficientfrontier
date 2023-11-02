#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install numpy')

import math
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize as sco


# In[2]:


stocks=['AAPL','TSLA','NVDA','GOOGL','AMZN','INTC','XOM']

eD=dt.datetime.today()
sD=eD-dt.timedelta(2*365)

price=yf.download(stocks,
                  period = '2y')['Adj Close'].pct_change()
returns=price
al=len(stocks)


# In[3]:


class Tools:
    def __init__(self,returns, assets):
        self.returns = returns
        self.assets = assets
 
    def simpleComp(self):
        self.tbl=pd.DataFrame(index=self.assets)
        self.tbl['Mean']=returns.mean()
        self.tbl['Variance']=returns.var()
        return(self.tbl.T)
   
    def correlation(self):
        self.tbl=pd.DataFrame(index=self.assets)
        self.corr=returns.corr()
        return(self.corr)
    


# In[4]:


tls=Tools(returns=returns, assets=stocks)

display(tls.simpleComp().T,tls.correlation())


# In[ ]:




