from machine import Pin
import utime
                                                      
#  led_g = Pin(22, Pin.OUT)

#  led_g.value(0)
button = Pin(19, Pin.In, PULL_UP)

while True:
    button.when_pressed == 0:
        print("Button is Pressed")
    else:
        print("Button is not Pressed")
utime.sleep(0.1) 

