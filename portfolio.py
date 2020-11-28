import os
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = 'USD'

base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
url_end = '?structure=array&convert=USD'
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

request = requests.get(base_url+'?CMC_PRO_API_KEY='+config.API_KEY, params=parameters)
results = request.json()
data = results['data']

pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    pairs[symbol] = url

print()
print("My Portfolio")
print()

portfolio_value = 0.00
last_updated = 0

table = PrettyTable(['Asset', 'Amount Owned',  parameters['convert'] + 'Value', 'Price', '1h', '24h', '7d' ])

with open('portfolio.txt') as inp:
    for line in inp:
        input_name, amount = line.split()
        input_name = input_name.upper()

        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY,
        }
        parameters = {
        'symbol': str(pairs[input_name])
        }
        inp_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest/' + url_end
        request = requests.get(inp_url+'?CMC_PRO_API_KEY='+config.API_KEY,params=parameters)
        results = request.json()

        currency = results['data'][0]
        rank = currency['cmc_rank']
        name = currency['name']
        last_updated = currency['last_updated']
        symbol = currency['symbol']
        quotes = currency['quote']
        hour_change = quotes[cryptocurrency]['percent_change_1h']
        day_change = quotes[cryptocurrency]['percent_change_24h']
        week_channge = quotes[cryptocurrency]['percent_change_7d']
        price = quotes[cryptocurrency]['price']

        Value = float(price) * float(amount)

        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.REST_ALL
        else: 
            hour_change = Back.RED + str(hour_change) + '%' + Style.REST_ALL
        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + '%' + Style.REST_ALL
        else: 
            day_change = Back.RED + str(day_change) + '%' + Style.REST_ALL
        if week_channge > 0:
            week_channge = Back.GREEN + str(week_channge) + '%' + Style.REST_ALL
        else: 
            week_channge = Back.RED + str(week_channge) + '%' + Style.REST_ALL

        portfolio_value += value

        value_string = '{:,}'.format(round(value,2))

        table.add_row([name + ' (' + symbol + ')',
                        '$' + value_string,
                        '$' + str(price),
                        str(hour_change),
                        str(day_change),
                        str(week_channge)])
print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value,2))

print("Total Portfolio Value: " + Back.GREEN + '$' + portfolio_value_string + Style.REST_ALL)
print()
print("API Results Last Updated on" + last_updated)