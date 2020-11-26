import json
import requests
import config 

latest_url = "https://pro-api.coinmarketcap.com/v1/key/info"

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}

request = requests.get(latest_url+'?CMC_PRO_API_KEY='+config.API_KEY)
results = request.json()
key_info = json.dumps(results, sort_keys=True, indent=4)

print(key_info)
print(type(results))


