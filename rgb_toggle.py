from machine import Pin
import utime

led_r = Pin(21, Pin.OUT)                                                       
led_g = Pin(18, Pin.OUT)
led_b = Pin(16, Pin.OUT)

led_r.value(0)
led_g.value(0)
led_b.value(0)

while True:
    led_r.toggle()
    utime.sleep(0.5)
    led_r.toggle()
    
    led_g.toggle()
    utime.sleep(0.5)
    led_g.toggle()
    
    led_b.toggle()
    utime.sleep(0.5)
    led_b.toggle()
    utime.sleep(0.5)
