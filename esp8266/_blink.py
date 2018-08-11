import machine
import time

def blink(sleep=1, pin=2):
    pin_ = machine.Pin(pin, machine.Pin.OUT)
    while True:
        pin_.off()
        time.sleep(sleep)
        pin_.on()
        time.sleep(sleep)


if __name__ == "__main__":
    blink()