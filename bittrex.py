#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:44:05 2017

@author: garrettlee
@documentation: https://www.kraken.com/en-us/help/api#general-usage
"""

import requests

def getOrders(pair, depth):
    url = 'https://bittrex.com/api/v1.1/public/getorderbook?market='+pair+'&type=both&depth='+depth
    r = requests.get(url)
    return r.json()
    
def topAskBid(pair):
    orders = getOrders(pair, '1')['result']
    ask = float(orders['sell'][0]['Rate'])
    bid = float(orders['buy'][0]['Rate'])
    return ask, bid


"""
bittrex = {}
r = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries')
r = r.json()
c = requests.get('https://bittrex.com/api/v1.1/public/getcurrencies').json()
a = pd.DataFrame(c['result'])
a = a.set_index('Currency')
for dic in r['result']:
    coins = dic['MarketName'].split('-')
    bittrex[str(a.ix[coins[1]]['CurrencyLong']+'-'+a.ix[coins[0]]['CurrencyLong']).lower()] = dic['MarketName']
"""