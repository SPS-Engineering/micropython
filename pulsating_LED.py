from machine import Pin, PWM
import utime

led_red = machine.Pin(28)
led_pwm = PWM(led_red)
duty_step = 129

frequency = 5000
led_pwm.freq (frequency)

while True:
    for duty_cycle in range(0, 65536, duty_step):
        led_pwm.duty_u16(duty_cycle)
        utime.sleep(0.005)
    for duty_cycle in range(65536, 0, -duty_step):
        led_pwm.duty_u16(duty_cycle)
        utime.sleep(0.005)
