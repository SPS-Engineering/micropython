from machine import Pin
import utime

button = Pin(14, Pin.IN, Pin.PULL_UP)
led_g = Pin(16, Pin.OUT)

while True:
    if button.value() == 0:
        led_g.value(1)
    else:
        led_g.value(0)
    utime.sleep(0.1)
