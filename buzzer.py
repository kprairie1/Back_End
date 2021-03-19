import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 24
GPIO.setup(buzzer, GPIO.OUT)

while true:
	GPIO.output(buzzer, GPIO.HIGH)
	print("Beep")
	sleep(0.5)
	
	GPIO.output(buzzer, GPIO.LOW)
	print("No Beep")
	sleep(0.5)
