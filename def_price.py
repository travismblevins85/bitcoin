import pandas_datareader as web
from datetime import date
from datetime import timedelta

def getPercent():
    coinList = ("BTC-USD", "ETH-USD", "LTC-USD")
    # Coins I need to add to Yahoo to print