import json
import requests
import config 

latest_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {
  'start':'1',
  'limit':'2',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}

request = requests.get(latest_url+'?CMC_PRO_API_KEY='+config.API_KEY, params=parameters)
results = request.json()

active_name = results["data"][0]["name"]
active_rank = results['data'][0]['cmc_rank']
active_symbol = results['data'][0]['symbol']
active_updated = results['data'][0]['last_updated']
active_price = int(results['data'][0]['quote']['USD']['price'])
active_1h = format(float(results['data'][0]['quote']['USD']['percent_change_1h']),".2f")
active_24h = format(float(results['data'][0]['quote']['USD']['percent_change_24h']),".2f")

# Single request 
print('Cryptocurrency name is ' + active_name + ' ('+active_symbol+') ' + 'ranked at ' + str(active_rank) + ' of all cryptocurrency. Priced at ' + str(active_price)+ ' currently trending at ' + str(active_1h) + ' for the last hour and ' + str(active_24h)+ ' for the last 24 hours.' ) 
print('This was last updated ' +str(active_updated))

#format the json data
crypto = json.dumps(results, sort_keys=True, indent=4)
print(crypto)
print(type(crypto))

# Parse the json data
data = results["data"]
for crypto in data:
    print('Cryptocurrency name is ' + crypto["name"] + ' ('+crypto["symbol"]+') ' + 'ranked at ' + str(crypto["cmc_rank"]) + ' of all cryptocurrency. Priced at ' + str(crypto['quote']['USD']['price'])+ ' currently changing at ' + str(format(float(crypto['quote']['USD']['percent_change_1h']),".2f")) + ' for the last hour and ' + str(format(float(crypto['quote']['USD']['percent_change_24h']),".2f"))+ ' for the last 24 hours.' ) 
    print('This was last updated ' +str(crypto["last_updated"]))




