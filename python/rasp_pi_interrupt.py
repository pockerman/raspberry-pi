# Code adapted from
# Raspberry Pi Cookbook Software and Hardware Problems and Solutions, 2nd Edition, O Reilly
# by Simon Monk

import RPi.GPIO as GPIO
import time


def callback(channel):
	print("state changed...")


def main():

	counter = 0
	while True:
		counter += 1
		print(counter)
		time.sleep(1)
		
	
if __name__ == '__main__':

	PIN = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# The function will be called if the GPIO pin 
	# goes from high to low. We can also set GPIO.RISING.
	# Then the function will be called when the input goes from
	# low to high
	GPIO.add_event_detect(PIN, GPIO.FALLING, callback=callback)
	
	try:
		main(pin=PIN)
    finally:
        GPIO.cleanup()
	except KeyboardInterrupt:
        print("Example stopped by user")

