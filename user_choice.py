import json
import requests
import config 

base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}
parameters = {
  'start':'1',
  'limit':'2',
  'sort': 'name', #symbol #price
  'convert':'USD'
}
choice = input("Do you want to enter any custom parameters? (y/n):")

if choice == 'y':
    parameters['limit'] = input('How many would you like displayed?: ')
    parameters['start'] = input('When would you like it to start?: ')
    parameters['sort'] = input('What do you want to sort by?: ')
    parameters['convert'] = input('What is your local currency?: ')

request = requests.get(base_url+'?CMC_PRO_API_KEY='+config.API_KEY, params=parameters)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']
cryptocurrency = parameters['convert']
for currency in data:
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = int(currency['circulating_supply'])
    total_supply = int(currency['total_supply'])

    quotes = currency['quote']
    market_cap = quotes[cryptocurrency]['market_cap']
    hour_change = quotes[cryptocurrency]['percent_change_1h']
    day_change = quotes[cryptocurrency]['percent_change_24h']
    week_change = quotes[cryptocurrency]['percent_change_7d']
    price = quotes[cryptocurrency]['price']
    volume = quotes[cryptocurrency]['volume_24h']

    print(str(rank) + ': ' + name + ' (' + symbol + ')')
    print('Price: \t\t$' + str(price))
    print('Market cap: \t\t$' + str(market_cap))
    print('24h Volume: \t\t$' + str(week_change))
    print('Hour change: \t\t$' + str(week_change))
    print('Day change: \t\t$' + str(day_change))
    print('Total Supply: \t\t$' + str(total_supply))
    print('Circulating Supply: \t\t$' + str(circulating_supply))
    print()