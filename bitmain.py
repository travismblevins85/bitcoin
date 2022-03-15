import webbrowser
from datetime import datetime, timedelta, date
import pandas as pd
import plotly.graph_objects as go
import pandas_datareader as pdr

print("This project is to show you Bitcoin's influence over the rest of the crypto market, the majority of the market follows \nthe same trend, up or down.  I involved 3 or the main coins, Bitcoin, Ethereum (the top 2), and Litecoin.")
print("To display this, i have two graphs to show you the last 30 days trend, and an input/output to show the current price \ndifference in the 3 of the main coins in the last 24 hours.")
print("This is really just the beginning of this project, of many things to come, but many updates in the near future. .")


print("Would you like to see the first graph or skip to the next?  \nYes - shows the graph\nSkip - continues to the next graph")
if input == ("YES"):
    get_url= webbrowser.open("https://finance.yahoo.com/chart/BTC-USD#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJjYW5kbGVXaWR0aCI6MzQuOTM3NSwiZmxpcHBlZCI6ZmFsc2UsInZvbHVtZVVuZGVybGF5Ijp0cnVlLCJhZGoiOnRydWUsImNyb3NzaGFpciI6dHJ1ZSwiY2hhcnRUeXBlIjoibGluZSIsImV4dGVuZGVkIjpmYWxzZSwibWFya2V0U2Vzc2lvbnMiOnt9LCJhZ2dyZWdhdGlvblR5cGUiOiJvaGxjIiwiY2hhcnRTY2FsZSI6InBlcmNlbnQiLCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkJUQy1VU0QiLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCLigIx2b2wgdW5kcuKAjCJdfX0sImxpbmVXaWR0aCI6Miwic3RyaXBlZEJhY2tncm91bmQiOnRydWUsImV2ZW50cyI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwic3RyaXBlZEJhY2tncm91ZCI6dHJ1ZSwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZX0sInNpZ0RldiI6e319LCJjdXN0b21SYW5nZSI6eyJzdGFydCI6MTY0MTAxMzIwMDAwMCwiZW5kIjoxNjQzNjkxNjAwMDAwfSwic3ltYm9scyI6W3sic3ltYm9sIjoiQlRDLVVTRCIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJCVEMtVVNEIiwicXVvdGVUeXBlIjoiQ1JZUFRPQ1VSUkVOQ1kiLCJleGNoYW5nZVRpbWVab25lIjoiVVRDIn0sInBlcmlvZGljaXR5IjoxLCJpbnRlcnZhbCI6ImRheSJ9LHsic3ltYm9sIjoiRVRILVVTRCIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJFVEgtVVNEIn0sInBlcmlvZGljaXR5IjoxLCJpbnRlcnZhbCI6ImRheSIsImlkIjoiRVRILVVTRCIsInBhcmFtZXRlcnMiOnsiY29sb3IiOiIjNzJkM2ZmIiwid2lkdGgiOjIsImlzQ29tcGFyaXNvbiI6dHJ1ZSwic2hhcmVZQXhpcyI6dHJ1ZSwiY2hhcnROYW1lIjoiY2hhcnQiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiRVRILVVTRCJ9LCJwYW5lbCI6ImNoYXJ0IiwiZmlsbEdhcHMiOmZhbHNlLCJhY3Rpb24iOiJhZGQtc2VyaWVzIiwic3ltYm9sIjoiRVRILVVTRCIsImdhcERpc3BsYXlTdHlsZSI6InRyYW5zcGFyZW50IiwibmFtZSI6IkVUSC1VU0QiLCJvdmVyQ2hhcnQiOnRydWUsInVzZUNoYXJ0TGVnZW5kIjp0cnVlLCJoZWlnaHRQZXJjZW50YWdlIjowLjcsIm9wYWNpdHkiOjEsImhpZ2hsaWdodGFibGUiOnRydWUsInR5cGUiOiJsaW5lIiwic3R5bGUiOiJzdHhfbGluZV9jaGFydCIsImhpZ2hsaWdodCI6ZmFsc2V9fSx7InN5bWJvbCI6IkxUQy1VU0QiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiTFRDLVVTRCJ9LCJwZXJpb2RpY2l0eSI6MSwiaW50ZXJ2YWwiOiJkYXkiLCJpZCI6IkxUQy1VU0QiLCJwYXJhbWV0ZXJzIjp7ImNvbG9yIjoiI2FkNmVmZiIsIndpZHRoIjoyLCJpc0NvbXBhcmlzb24iOnRydWUsInNoYXJlWUF4aXMiOnRydWUsImNoYXJ0TmFtZSI6ImNoYXJ0Iiwic3ltYm9sT2JqZWN0Ijp7InN5bWJvbCI6IkxUQy1VU0QifSwicGFuZWwiOiJjaGFydCIsImZpbGxHYXBzIjpmYWxzZSwiYWN0aW9uIjoiYWRkLXNlcmllcyIsInN5bWJvbCI6IkxUQy1VU0QiLCJnYXBEaXNwbGF5U3R5bGUiOiJ0cmFuc3BhcmVudCIsIm5hbWUiOiJMVEMtVVNEIiwib3ZlckNoYXJ0Ijp0cnVlLCJ1c2VDaGFydExlZ2VuZCI6dHJ1ZSwiaGVpZ2h0UGVyY2VudGFnZSI6MC43LCJvcGFjaXR5IjoxLCJoaWdobGlnaHRhYmxlIjp0cnVlLCJ0eXBlIjoibGluZSIsInN0eWxlIjoic3R4X2xpbmVfY2hhcnQiLCJoaWdobGlnaHQiOmZhbHNlfX1dLCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQiLCJwYW5lbE5hbWUiOiJjaGFydCJ9fX0sInJhbmdlIjp7ImR0TGVmdCI6IjIwMjEtMTItMzFUMDU6MDA6MDAuMjMxWiIsImR0UmlnaHQiOiIyMDIyLTAyLTAyVDA0OjU5OjAwLjIzMVoiLCJwZXJpb2RpY2l0eSI6eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZCI6MX0sInBhZGRpbmciOjB9fQ--")
    open()


CRYPTOS = ['BTC', 'ETH', 'LTC',]
CURRENCY = 'USD'

def getData(cryptocurrency):
    now = date.today()
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


print("""Last but not least, I have a small Yahoo! output, showing the change in price within the last 24 hours.  If my theory is correct\n
then the price differences should be around the same.  Let's find out.""")

btc = pdr.get_data_yahoo('BTC-USD',start=date.today() - timedelta(hours=24), end = date.today())
eth = pdr.get_data_yahoo('ETH-USD',start=date.today() - timedelta(hours=24), end = date.today())
ltc = pdr.get_data_yahoo('LTC-USD',start=date.today() - timedelta(hours=24), end = date.today())



x = ((btc["Adj Close"])[1] - (btc["Adj Close"])[0]) / (btc["Adj Close"])[0] * 100
y = ((eth["Adj Close"])[1] - (eth["Adj Close"])[0]) / (eth["Adj Close"])[0] * 100
z = ((ltc["Adj Close"])[1] - (ltc["Adj Close"])[0]) / (ltc["Adj Close"])[0] * 100
print("Bitcoin's daily percentage change is : ", x)
print("Ethereum's daily percentage change is : ", y)
print("Litecoins's daily percentage change is : ", z)
