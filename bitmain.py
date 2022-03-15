from datetime import date, timedelta
import pandas as pd
import plotly.graph_objects as go
import pandas_datareader as pdr

btc_inf = ("Bitcoin's Influence")
bt = btc_inf.center(120, '-')
print(bt)
print("-This project is to show you Bitcoin's influence over the rest of the crypto market, the majority of the market follows \nthe same trend, up or down.  I involved 3 of the main coins, Bitcoin, Ethereum (the top 2), and Litecoin.")
print ("\n-To display this, I have a graph to show you the last last 365 days of price trendlines.  I also have have a current\n24 hour percentage change of each coin, which  most likely will be similar.  Many, many updates in the future :)")
print("\n-Relevance being, is Litecoin is closely related to Bitcoin, but Ethereum is Bitcoin's #1 competitor.")

names = ("Bitcoin, Ethereum, & Litecoin")
n=names.center(120,'-')
print(n)
print("-Bitcoin is a decentralized cryptocurrency originally described in a 2008 whitepaper by a person, or group of people, using the alias Satoshi Nakamoto. It was launched soon after, in January 2009.  Bitcoin is a peer-to-peer online currency, meaning that all transactions happen directly between equal, independent network participants, without the need for any intermediary to permit or facilitate them. Bitcoin was created, according to Nakamoto’s own words, to allow \"online payments to be sent directly from one party to another without going through a financial institution.\"Some concepts for a similar type of a decentralized electronic currency precede BTC, but Bitcoin holds the distinction of being the first-ever cryptocurrency to come into actual use.")
print("\n-Ethereum is a decentralized open-source blockchain system that features its own cryptocurrency, Ether. ETH works as a platform for numerous other cryptocurrencies, as well as for the execution of decentralized smart contracts.  Ethereum was first described in a 2013 whitepaper by Vitalik Buterin. Buterin, along with other co-founders, secured funding for the project in an online public crowd sale in the summer of 2014. The project team managed to raise $18.3 million in Bitcoin, and Ethereum’s price in the Initial Coin Offering (ICO) was $0.311, with over 60 million Ether sold. Taking Ethereum’s price now, this puts the return on investment (ROI) at an annualized rate of over 270%, essentially almost quadrupling your investment every year since the summer of 2014.  The Ethereum Foundation officially launched the blockchain on July 30, 2015, under the prototype codenamed “Frontier.” Since then, there has been several network updates — “Constantinople” on Feb. 28, 2019, “Istanbul” on Dec. 8, 2019, “Muir Glacier” on Jan. 2, 2020, “Berlin” on April 14, 2021, and most recently on Aug. 5, 2021, the “London” hard fork.  Ethereum’s own purported goal is to become a global platform for decentralized applications, allowing users from all over the world to write and run software that is resistant to censorship, downtime and fraud.")
print("\n-Litecoin (LTC) is a cryptocurrency that was designed to provide fast, secure and low-cost payments by leveraging the unique properties of blockchain technology.  To learn more about this project, check out our deep dive of Litecoin.  The cryptocurrency was created based on the Bitcoin (BTC) protocol, but it differs in terms of the hashing algorithm used, hard cap, block transaction times and a few other factors. Litecoin has a block time of just 2.5 minutes and extremely low transaction fees, making it suitable for micro-transactions and point-of-sale payments.  Litecoin was released via an open-source client on GitHub on Oct. 7, 2011, and the Litecoin Network went live five days later on Oct. 13, 2011. Since then, it has exploded in both usage and acceptance among merchants and has counted among the top ten cryptocurrencies by market capitalization for most of its existence.  The cryptocurrency was created by Charlie Lee, a former Google employee, who intended Litecoin to be a \"lite version of Bitcoin,\" in that it features many of the same properties as Bitcoin—albeit lighter in weight.")

graph = ("Trendline Graph")
trend = graph.center(120,'-')
print(trend)

CRYPTOS = ['BTC', 'ETH', 'LTC',]
CURRENCY = 'USD'

def getData(cryptocurrency):
    now = date.today()
    #Keep it current with today whenever used
    today = now.strftime("%Y-%m-%d")
    #Go back a month
    month_earlier = (now - timedelta(days=365)).strftime("%Y-%m-%d")

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
        title ="Bitcoin's influence over other cryptos,notice the similar trendlines over a year.",
        title_x=0.5,
        xaxis_title = 'Date',
        yaxis_title = f'Closing price ({CURRENCY})',
          legend_title = 'Cryptos'
    )
fig.update_yaxes(type='log', tickprefix='$')

fig.show()

per = ("Daily Percentage Change")
cent = per.center(120,'-')
print(cent)

print("""Last but not least, I have a small Yahoo! output, showing the change in price within the last 24 hours.  If my theory is correct\n
then the price differences should be around the same.  Let's find out.""")

btc = pdr.get_data_yahoo('BTC-USD',start=date.today() - timedelta(hours=24), end = date.today())
eth = pdr.get_data_yahoo('ETH-USD',start=date.today() - timedelta(hours=24), end = date.today())
ltc = pdr.get_data_yahoo('LTC-USD',start=date.today() - timedelta(hours=24), end = date.today())


x = ((btc["Adj Close"])[1]-(btc["Adj Close"])[0]) / (btc["Adj Close"])[0] * 100
y = ((eth["Adj Close"])[1]-(eth["Adj Close"])[0]) / (eth["Adj Close"])[0] * 100
z = ((ltc["Adj Close"])[1]-(ltc["Adj Close"])[0]) / (ltc["Adj Close"])[0] * 100
print("Bitcoin's daily percentage change is : ", x)
print("Ethereum's daily percentage change is : ", y)
print("Litecoins's daily percentage change is : ", z)
