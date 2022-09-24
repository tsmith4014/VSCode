import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

# dict_ ={'a':[11,21,31], 'b':[12,22,32]}

# df=pd.DataFrame(dict_)

# print(df.head())
# print(df.mean())

cg = CoinGeckoAPI()

bitcoinData = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

#print(type(bitcoin_data), pd.DataFrame(bitcoin_data).head())

bitcoinPriceData = bitcoinData['prices']

#print(bitcoinPriceData[0:5])

data = pd.DataFrame(bitcoinPriceData, columns=['TimeStamp', 'Price'])

data['date'] =  data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

#print(data)

candlestickData = data.groupby(data.date, as_index=False).agg({'Price': ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=candlestickData['date'],open=candlestickData['Price']['first'], high=candlestickData['Price']['max'],  low=candlestickData['Price']['min'], close=candlestickData['Price']['last'])])
fig.update_layout(xaxis_rangeslider_visible=False)

print(fig.show())