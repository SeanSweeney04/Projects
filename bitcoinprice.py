import requests
# This is the first API I have ever made, which retrieves Bitcoin's current price.
response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
price = response.json()
bitcoin_price = price['bitcoin']['usd']

print("Bitcoin is currently priced at $",bitcoin_price)
