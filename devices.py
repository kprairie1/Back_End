# Import Required Libaries
import RPi.GPIO as GPIO
import time
import pyaudio
import wave
import socket
import sys

# Set pin #'s, Pin Modes, Button Event, PyAudio settings
def startSetup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	button = 23
	LED = 24
	buzzer = 25
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(button, GPIO.RISING, callback=button_callback)
	GPIO.setup(LED, GPIO.OUT)
	GPIO.setup(buzzer, GPIO.OUT)
	
	form_1 = pyaudio.paInt16
	audio = pyaudio.PyAudio()
	numChannels = 1
	sample_rate = 44100
	chunk = 4096
	record_secs = 10

# Function that occurs when the button is pressed	
def buttonCallback():
	print("Button was pressed")
	#connection.sendall("Button was pressed")

# Play buzzer
def startBuzzer(buzzer):
	GPIO.output(buzzer, GPIO.HIGH)
	print("Beep")

# Stop buzzer and pause for 1 second	
def stopBuzzer(buzzer):
	GPIO.output(buzzer, GPIO.LOW)
	print("No Beep")

# Toggle buzzer 4 times	
def toggleBuzzer(buzzer):
	stopBuzzer(buzzer)
	
	for i in range(1, 5):
		startBuzzer(buzzer)
		sleep(0.5)
		stopBuzzer(buzzer)
		sleep(0.5)

# Turn LED On	
def startLED(LED):
	print("LED on")
	GPIO.output(LED, GPIO.HIGH)

# Turn LED Off
def stopLED(LED):
	print("LED off")
	GPIO.output(LED, GPIO.LOW)

# Toggle LED 4 times	
def toggleLED(LED):
	stopLED(LED)
	
	for i in range(1, 5):
		startLED(LED)
		sleep(0.5)
		stopLED(LED)
		sleep(0.5)

# Start Microphone and record for 10 seconds
# Then save to a .wav file		
def startMicrophone():
	for i in range(audio.get_device_count()):
		if("USB" in p.get_device_info_by_index(i).get('name')):
			index = i
			break

	stream = audio.open(format = form_1, rate = sample_rate, channels = numChannels, 
						input_device_index = index, input = True, frames_per_buffer = chunk)

	print("Recording")
	frames = []

	for i in range (0, int((sample_rate/chunk) * record_secs)):
		data = stream.read(chunk)
		frames.append(data)
		
	print("Finished Recording")

	stream.stop_stream()
	stream.close()
	audio.terminate()

	wavefile = wave.open("Test.wav", 'wb')
	wavefile.setnchannels(numChannels)
	wavefile.setsampwidth(audio.get_sample_size(form_1))
	wavefile.writeframes(b''.join(frames))
	wavefile.close()
