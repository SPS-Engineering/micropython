from machine import Pin
import utime

button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("Button is Pressed")
    else:
        print("Button is not Pressed")
    utime.sleep(0.1)
