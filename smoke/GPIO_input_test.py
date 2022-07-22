#!/usr/bin/python
#encoding=utf-8

# the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).

import time
import datetime
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
    print('Gas Detected! Gas Detected!')
    return

endTime = datetime.datime.now() + datetime.timedelta(seconds=15)
while True:
  if datetime.datetime.now() >= endTime:
	break 
GPIO.add_event_detect(22, GPIO.RISING)
GPIO.add_event_callback(22, action)

try:
    while True:
        print('alive')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
