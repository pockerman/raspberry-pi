# Code adapted from
# Raspberry Pi Cookbook Software and Hardware Problems and Solutions, 2nd Edition, O Reilly
# by Simon Monk

import RPi.GPIO as GPIO
import time

def buzz(pin, pitch, duration):
	period = 1.0 / pitch
	delay = period /2.0

	cycles = int(duration * pitch)
	for i in range(cycles):
		GPIO.output(pin, True)
		time.sleep(delay)
		GPIO.output(pin, False)
		time.sleep(delay)
		
	
def main(pin):
	
	while True:
		pitch_s = input("Pitch: (200-2000): ")
		pitch = float(pitch_s)
		dur_s = input("Duration (secs): ")
		dur = float(dur_s)
		buzz(pin=pin, pitch=pitch, duration=dur)

if __name__ == '__main__':
	
	BUZZER_PIN = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_PIN, GPIO.OUT)

	try:
		main(pin=BUZZER_PIN)
    finally:
        GPIO.cleanup()
	except KeyboardInterrupt:
        print("Buzzer stopped by user")
