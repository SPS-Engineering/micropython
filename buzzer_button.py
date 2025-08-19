from machine import Pin
import utime
 
button = Pin(9, Pin.IN, Pin.PULL_UP)
buzzer = Pin(5, Pin.OUT)
 
while True:
    if button.value() == 0:
        buzzer.value(1)
        utime.sleep(1)
    else:
        buzzer.value(0)
