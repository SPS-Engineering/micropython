from machine import Pin, ADC
import utime

ldr = ADC(28) 
led_red = Pin(22, Pin.OUT)

led_green = Pin(20, Pin.OUT)

led_blue = Pin(18, Pin.OUT)

THRESHOLD_r = 4000
THRESHOLD_g = 1000

while True:
    digital_value = ldr.read_u16()  
    print("ADC value=",digital_value)   
    if digital_value > THRESHOLD_r:
        led_red.value(1)
        led_green.value(0)
        led_blue.value(0)
    elif THRESHOLD_g < digital_value < THRESHOLD_r:
        led_red.value(0)
        led_green.value(1)
        led_blue.value(0)    
    elif digital_value < THRESHOLD_g:
        led_red.value(0)
        led_green.value(0)
        led_blue.value(1)    
    utime.sleep(0.5)
