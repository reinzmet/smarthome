import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

try:
	while True:
		GPIO.output(5, GPIO.HIGH)
		time.sleep(4)
		GPIO.output(5, GPIO.LOW)
		GPIO.output(10, GPIO.HIGH)
		time.sleep(4)
		GPIO.output(10, GPIO.LOW)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(4)
		GPIO.output(13, GPIO.LOW)

except KeyboardInterrupt:
	print ("\n Keyboard interrupt has been detected")

except:
	print("An error has occured")

finally:
	GPIO.cleanup()
