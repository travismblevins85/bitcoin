from prettytable import PrettyTable
import requests

r = requests.get("https://api.coinmarketcap.com/v1/ticker/")
data = r.json()

x = PrettyTable()
x.field_names = [ "Bitcoin", "BTC", "Price in USD"]

for crypto in data:
    x.add_row([ crypto['Bitcoin'], crypto['BTC'], crypto['price_usd'] ])

print(data)```