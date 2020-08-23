import RPi.GPIO as GPIO
import time

def main(led_pin):

	pwm_led = GPIO.PWM(led_pin, 500)
    pwm_led.start(100)
    
    while True:
        duty = input("LED brightness (0, 100):")
        
        duty = int(duty)
        
        if duty > 100:
            print("WARNING: Duty cycle larger than 100. Setting to 100")
            duty = 100
            
        if duty < 0:
            print("WARNING: Duty cycle less than 0. Setting to 0")
            duty = 0
            
        pwm_led.ChangeDutyCycle(duty)

    
if __name__ == '__main__':

    LED_PIN = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_PIN, GPIO.OUT)

	try:
		main(led_pin=LED_PIN)
    finally:
        GPIO.cleanup()
	except KeyboardInterrupt:
        print("LED flash stopped by user")
