from time import sleep
from gpiozero import LightSensor, Buzzer

ldr = LightSensor(7)
while True:
	print(ldr.value)
	sleep(1.5)
