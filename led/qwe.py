import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

try:
        while True:
                GPIO.output(19, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(19, GPIO.LOW)
                
                GPIO.output(11, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(11, GPIO.LOW)
                
                GPIO.output(22, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(22, GPIO.LOW)
                


except KeyboardInterrupt:
        print "\nA keyboard interrupt has been noticed"

except:
        print "An error has occured!"
finally:
        GPIO.cleanup()

