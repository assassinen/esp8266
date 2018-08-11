from esp8266._oled import print_test, set_string, show, fill
from esp8266._network import get_info_network
from bitfinex.tikers import get_last_price
import time


def get_data(symbols):
    # data = get_last_price(symbols)
    data_hist = [[{'SYMBOL': None, 'LAST_PRICE': None}]]
    # if len(data) > 0:
    #     set_string('from BITFINIX', 1, 5)
    #     data_hist[0] = data
    # else:
    set_string('from HISTORY', 1, 5)
    # data = data_hist[0]
    return data_hist[0]


def main():
    symbols = ('tBTCUSD', 'tETHUSD', 'tETHBTC')
    while True:
        n = 0
        fill()
        data = get_last_price(symbols)

        if len(data) > 0:
            set_string('from BITFINIX', n, 5)
            n += 1
            for coin_params in data:
                n += 1
                set_string("{}: {}".format(coin_params['SYMBOL'][1:], coin_params['LAST_PRICE']), n)

        else:
            set_string('no Data', n, 0)
            for i in get_info_network('STA'):
                n += 1
                set_string(i, n)

        set_string("works {} sec".format(time.time()), 5, 5)

        show()
        time.sleep(3)


if __name__ == "__main__":
    main()

