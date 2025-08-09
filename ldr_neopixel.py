from machine import Pin, ADC
import neopixel
import utime

ldr = ADC(28) 
NEOPIXEL_PIN = 18
NUM_PIXELS = 1

np = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN), NUM_PIXELS)

def set_pixel_grb(target_g, target_r, target_b, brightness=1.0):
    if not 0.0 <= brightness <= 1.0:
        print("Warning: Brightness factor must be between 0.0 and 1.0")
        brightness = 1.0
    
    g = int(target_g * brightness)
    r = int(target_r * brightness)
    b = int(target_b * brightness)
    
    g = max(0, min(255, g))
    r = max(0, min(255, r))
    b = max(0, min(255, b))
    
    for i in range(NUM_PIXELS):
        np[i] = (g, r, b)

    np.write()

while True:
    digital_value = ldr.read_u16()  
    print("ADC value=",digital_value)   
    brightness_ldr=1-(digital_value/65535)
    brightness_ldr = max(0.0, min(1.0, brightness_ldr))
    set_pixel_grb(target_g=255, target_r=0, target_b=0, brightness=brightness_ldr)
    utime.sleep(0.1)
