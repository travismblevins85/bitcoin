

import pandas_datareader as web
from datetime import date
from datetime import timedelta

now = date.today()

yesterday = now - timedelta(hours=24)


start = yesterday
end = now

ltc = web.DataReader('LTC-USD', 'yahoo',start,end)
percent = ((ltc['Adj Close'][1] - ltc['Close'][0]) / ltc['Close'][0] * 100)

print(ltc)
print("Litecoin's percentage change since 24 hours ago:", percent)