import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

try:
	while True:
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(22, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(19, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(19 ,GPIO.HIGH)			
		GPIO.output(11 ,GPIO.HIGH)
		GPIO.output(22 ,GPIO.HIGH)
		GPIO.output(11 ,GPIO.HIGH)
		GPIO.output(19 ,GPIO.HIGH)

finally:
	GPIO.cleanup()
