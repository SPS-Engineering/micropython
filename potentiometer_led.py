from machine import Pin, ADC
import utime

potentiometer_pin = Pin(26, Pin.IN)
adc = ADC(potentiometer_pin)
led = Pin(22, Pin.OUT)

THRESHOLD = 400

while True:
    potentiometer_value = adc.read_u16()
    print(potentiometer_value)
    if potentiometer_value < THRESHOLD:
        led.value(1)
    else:
        led.value(0)
    utime.sleep(0.1)
