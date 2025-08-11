from machine import Pin
from utime import ticks_ms, sleep
from random import randint

button = Pin(16, Pin.IN, Pin.PULL_UP)
led_g = Pin(22, Pin.OUT)

while True:
    print("Get ready...")
    sleep(randint(1,10))
    led_g.value(1)
    start = ticks_ms()
    while button.value() == 1:
        pass
    end = ticks_ms()
    led_g.value(0)
    while button.value() == 0:
        pass
    print("Reaction time: {} milliseconds".format(end - start))
    sleep(2)
