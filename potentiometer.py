from machine import Pin, ADC
import utime

pot = ADC(26) 

while True:
    digital_value = pot.read_u16()  
    print("Potentiometer value=",digital_value)
    utime.sleep(0.1)
