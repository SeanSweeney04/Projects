import requests

# This is an improvement on the Bitcoin API
# Simply type the price of the coin that you want, and it will retrieve the price for you

base_url = "https://api.coingecko.com/api/v3/simple/price?ids="

coin = input()
try:
   api = f'{base_url}{coin}&vs_currencies=usd'
   response = requests.get(api)
   price = response.json()
   coin_price = price[coin]['usd']
   print(f'{coin} is currently priced at ${coin_price}')

except:
   print("Coin not found")
      
