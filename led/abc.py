import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

try:
        while True:
                GPIO.output(11, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(11, GPIO.LOW)
                time.sleep(5)

except KeyboardInterrupt:
        print "\nA keyboard interrupt has been noticed"

except:
        print "An error has occured!"
finally:
        GPIO.cleanup()

