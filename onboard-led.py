import machine

led_pico = machine.Pin(25, machine.Pin.OUT)
led_pico.value(1)
