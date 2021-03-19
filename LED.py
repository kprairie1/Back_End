import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 25
GPIO.setup(LED, GPIO.OUT)

while True:
	print("LED on")
	GPIO.output(LED, GPIO.HIGH)
	time.sleep(1)

	print("LED off")
	GPIO.output(LED, GPIO.LOW)
