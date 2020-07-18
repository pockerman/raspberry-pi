import RPi.GPIO as GPIO
import time

if __name__ == '__main__':

	ENABLE_PIN = 18
	IN1_PIN = 23
	IN2_PIN = 24

	# set up GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(ENABLE_PIN, GPIO.OUT)
	GPIO.setup(IN1_PIN, GPIO.OUT)
	GPIO.setup(IN2_PIN, GPIO.OUT)

