import machine
import utime

led_red = machine.Pin(27, machine.Pin.OUT)

led_green = machine.Pin(20, machine.Pin.OUT)

led_blue = machine.Pin(16, machine.Pin.OUT)

while True:
    led_red.value(1)
    utime.sleep(1)
    led_red.value(0)
    utime.sleep(1)
    led_green.value(1)
    utime.sleep(1)
    led_green.value(0)
    utime.sleep(1)
    led_blue.value(1)
    utime.sleep(1)
    led_blue.value(0)
    utime.sleep(1)
