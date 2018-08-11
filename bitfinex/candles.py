import urequests as requests
import time

url = 'https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/last'


def get_last_candle():
    response = requests.get(url)
    return response.json()

def get_last_price():
    return get_last_candle()[2]
