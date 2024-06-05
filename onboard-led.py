import machine

led_pico = machine.Pin(22, machine.Pin.OUT)
led_pico.value(1)
