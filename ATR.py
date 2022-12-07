import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas as pd 
import plotly.graph_objects as go
import calendar
import requests

symbol='BTCUSD' #symbol to be traded
tick_interval = '1' #candle in minutes

now = dt.datetime.utcnow()
unixtime = calendar.timegm(now.utctimetuple())
since = unixtime
start = str(since - 60 * 60 * int(tick_interval))    
url = 'https://api.bybit.com/v2/public/kline/list?symbol='+symbol+'&interval='+tick_interval+'&from='+str(start)
data = requests.get(url).json()
D = pd.DataFrame(data['result'])

a = 1 
c = 10 

high_low = D['high'].astype(float) - D['low'].astype(float)
high_close = np.abs(D['high'].astype(float) - D['close'].astype(float).shift())
low_close = np.abs(D['low'].astype(float) - D['close'].astype(float).shift())
ranges = pd.concat([high_low, high_close, low_close], axis=1)
true_range = np.max(ranges, axis=1)

atr_indicator = true_range.rolling(c).sum()/c
nLoss = atr_indicator * a

print("############ ATR ############")
print(atr_indicator)
print("#############################")
