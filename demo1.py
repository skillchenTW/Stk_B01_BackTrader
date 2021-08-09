#_*_ coding:utf-8 _*_
# Date,Open,High,Low,Close,Adj Close,Volume

#from __future__ import(absolute_import, division, print_function,unicode_literals)
import datetime
import backtrader as bt
from backtrader import cerebro
import pandas as pd

# 空倉策略
class MyStrategy(bt.Strategy):
    pass


# 1.Create a cerebro
cerebro = bt.Cerebro()

# 2.Add Data Feed
# 2.1 Create a data feed
df = pd.read_csv('data/TW2330.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
#df['openinterest'] = 0
# brf_daily = bt.feeds.PandasData(dataname=df,
#     fromdate=datetime.datetime(2020,1,1),
#     todate=datetime.datetime(2021,8,9))

# 自定義CSV的資料欄位
# Date,Open,High,Low,Close,Adj Close,Volume
brf_daily = bt.feeds.GenericCSVData(
    dataname="data/TW2454.csv",
    fromdate=datetime.datetime(2020,1,1),
    todate=datetime.datetime(2021,8,9),
    nullvalue=0.0,
    dtformat=("%Y-%m-%d"),
    datetime=0,
    open=1,
    high=2,
    low=3,
    close=5,
    volume=6,
    #openinterest=-1
)    

# 2.2 Add the Data Feed to Cerebro
cerebro.adddata(brf_daily)

# 3. Add Strategy
cerebro.addstrategy(MyStrategy)

# 4. Run 
cerebro.run()

# 5. Plot result
# 最基本的線性圖
# cerebro.plot()
# 設定為蠟燭圖Candle
cerebro.plot(style="candle")