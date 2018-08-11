import urequests as requests
import time

url = 'https://api.bitfinex.com/v2/tickers?symbols={}'

key = [
    'SYMBOL',
    'BID',
    'BID_SIZE',
    'ASK',
    'ASK_SIZE',
    'DAILY_CHANGE',
    'DAILY_CHANGE_PERC',
    'LAST_PRICE',
    'VOLUME',
    'HIGH',
    'LOW'
]

def get_tikers(symbols=('tBTCUSD','tETHUSD',)):
    result = []
    try:
        response = requests.get(url.format(','.join(symbols)))
        if response.status_code == 200:
            result = [dict(zip(key, item)) for item in response.json()]
    except:
        return result
    return result



def get_last_price(symbols=('tBTCUSD','tETHUSD',)):
    key_list = ('SYMBOL', 'LAST_PRICE')
    result = [{key:item for key, item in tiker.items() if key in key_list} for tiker in get_tikers(symbols)]
    return result