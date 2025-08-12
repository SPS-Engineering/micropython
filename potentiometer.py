from machine import Pin, ADC
import utime

potentiometer_pin = Pin(26, Pin.IN)
adc = ADC(potentiometer_pin)


while True:
    potentiometer_value = adc.read_u16()
    print(potentiometer_value)
    utime.sleep(0.1)
