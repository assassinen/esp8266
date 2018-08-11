from esp8266 import _network
from machine import Pin, I2C
import ssd1306, time

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)


def print_test(message = 'hello, oled'):
    oled.fill(0)
    oled.text(message, 10, 0)
    oled.show()


def set_string(message ='None', string_number = 0, string_shift = 0):
    string_higt = 10
    pos = string_higt * string_number + string_shift
    oled.text(message, 0, pos)


def print_network_info(network_type=None):
    oled.fill(0)
    n = 0
    l = 'Home WiFi:' if network_type == 'STA' else 'Ad-hoc:'
    set_string(l, n)
    network_info = _network.get_info_network(network_type)

    for i in network_info:
        n += 1
        set_string(i, n)
        time.sleep(1)
    oled.show()

def fill():
    oled.fill(0)

def show():
    oled.show()