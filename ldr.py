from machine import ADC
import utime

ldr = ADC(28) 

while True:
    digital_value = ldr.read_u16()     
    print("ADC value=",digital_value)
    volt=3.3*(digital_value/65535)
    print("Voltage: {}V ".format(volt))
    utime.sleep(1)
