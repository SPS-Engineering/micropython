import machine
import utime

led-pico = machine.Pin(25, machine.Pin.OUT)

while True:
  led-pico.value(1)
  utime.sleep(2)
  led-pico.value(0)
  utime.sleep(2)
