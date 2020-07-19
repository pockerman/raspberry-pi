import RPi.GPIO as GPIO
import time

def turn_clockwise(in1_pin, in2_pin):
	GPIO.output(in1_pin, True)
	GPIO.output(in2_pin, False)

def turn_anticlockwise(in1_pin, in2_pin):
	GPIO.output(in1_pin, False)
	GPIO.output(in2_pin, True)


if __name__ == '__main__':

	ENABLE_PIN = 18
	IN1_PIN = 23
	IN2_PIN = 24

	# set up GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(ENABLE_PIN, GPIO.OUT)
	GPIO.setup(IN1_PIN, GPIO.OUT)
	GPIO.setup(IN2_PIN, GPIO.OUT)

	# set up the speed to the spin
	pwm = GPIO.PWM(ENABLE_PIN, 100)
	pwm.start(0)

	while True:

		try:
			turn_clockwise(in1_pin=IN1_PIN, in2_pin=IN2_PIN)
			time.sleep(1)
			turn_anticlockwise(in1_pin=IN1_PIN, in2_pin=IN2_PIN)
			time.sleep(1)
		except  KeyboardInterrupt:
			break

	# cleanup the pins
	GPIO.cleanup()

		

