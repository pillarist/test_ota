from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT) # change the pin number according to your board

while True:
    led.value(not led.value()) # toggle the LED state
    sleep(0.5) # wait for half a second
