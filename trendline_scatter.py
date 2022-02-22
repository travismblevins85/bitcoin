from datetime import datetime, timedelta

import pandas as pd
import pandas_datareader as pdr
import plotly.graph_objects as go
#List the 3 cryptos that i want to use
#Clarify which currency it is and remember to use it later
CRYPTOS = ['BTC', 'ETH', 'LTC',]
CURRENCY = 'USD'

def getData(cryptocurrency):
    now = datetime.now()
    #Keep it current with today whenever used
    today = now.strftime("%Y-%m-%d")
    #Go back a month
    month_earlier = (now - timedelta(days=30)).strftime("%Y-%m-%d")

    start = pd.to_datetime(month_earlier)
    end = pd.to_datetime(today)

    data = pdr.get_data_yahoo(f'{cryptocurrency}-{CURRENCY}', start, end)

    return data
#Use dict comprehension which at first is a little confusing to me
#but key:value for variable in iterable
crypto_data = dict()
for crypto in CRYPTOS:
    crypto_data[crypto] = getData(crypto)

fig = go.Figure()

    # Scatter
for idx, name in enumerate(crypto_data):
        fig = fig.add_trace(
            go.Scatter(
                x = crypto_data[name].index,
                y = crypto_data[name].Close,
                name = name,
            )
        )
# Center the top title with title_x, or center
fig.update_layout(
        title ='The influence of Bitcoin over other cryptos, notice the similar trend lines regardless to price differential.',
        title_x=0.5,
        xaxis_title = 'Date',
        yaxis_title = f'Closing price ({CURRENCY})',
        legend_title = 'Cryptos'
    )
fig.update_yaxes(type='log', tickprefix='$')

fig.show()

