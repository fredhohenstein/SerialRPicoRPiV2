#Source: Electrocredible.com, Language: MicroPython.

from machine import Pin,UART
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
uart.init(bits=8, parity=None, stop=1)
#led = Pin("LED", Pin.OUT)

while True:
    #uart.write('Hello from Pico')
    if uart.any(): 
        data = uart.read() 
        print(data)
#        if data== b'm':
#            led.toggle() 
    time.sleep(1)
    