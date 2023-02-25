# sender.py
import time
import serial

ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

msg = ""
i = 0

while True:
    i+=1
    print("Counter {} - Hello from TOTEMPI".format(i))
    ser.write('Hello from TOTEMPI'.encode('utf-8'))
    time.sleep(2)
