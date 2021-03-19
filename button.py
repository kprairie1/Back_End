import RPi.GPIO as GPIO

def button_callback(channel):
    print("Button was pushed!")
    
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
button = 23
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button, GPIO.RISING, callback=button_callback)
message = input("Press enter to quit\n\n")
GPIO.cleanup() 
