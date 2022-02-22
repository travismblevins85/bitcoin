#

import pandas_datareader as web
from datetime import date
from datetime import timedelta

now = date.today()

yesterday = now - timedelta(hours=24)


start = yesterday
end = now

btc = web.DataReader('BTC-USD', 'yahoo',start, end)

percent = ((btc['Adj Close'][1] - btc['Close'][0]) / btc['Close'][0] * 100)

print(btc)
print("Bitcoin's percentage change since 24 hours ago:", percent)