# 20141129 This program simulates the red, 
# yellow, green cycle of a traffic light.

import time 
import RPi.GPIO as GPIO 
 
GPIO.setmode(GPIO.BOARD) 

GPIO.setup(19, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(7, GPIO.OUT) 

try:
        while True:
                GPIO.output(19, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(11, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(11, GPIO.LOW)
                GPIO.output(7, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(7, GPIO.LOW) 

except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!") 

except:
    print("\nAn error or exception has occurred!") 

finally:
    GPIO.cleanup()
