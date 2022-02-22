

import pandas_datareader as web
from datetime import date
from datetime import timedelta

now = date.today()

yesterday = now - timedelta(hours=24)


start = yesterday
end = now

eth = web.DataReader('ETH-USD', 'yahoo',start, end)
percent = ((eth['Adj Close'][1] - eth['Close'][0]) / eth['Close'][0] * 100)

print(eth)
print("Ethereum's percentage change since 24 hours ago:", percent)