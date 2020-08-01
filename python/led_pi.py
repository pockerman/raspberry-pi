import RPi.GPIO as GPIO
import time

def main():

	while (True):
	GPIO.output(18, True)
	time.sleep(0.5)
	GPIO.output(18, False)
	time.sleep(0.5)

if __name__ == '__main__':

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)

	try:
		main()
	except KeyboardInterrupt:
        print("LED flash stopped by user")
        GPIO.cleanup()
		


