#Libraries
import RPi.GPIO as GPIO
import time
 

def distance(trigger, echo):

    # set Trigger to HIGH
    GPIO.output(trigger, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)
 
    statt_time = time.time()
    stop_time = time.time()
 
    # save StartTime
    while GPIO.input(echo) == 0:
        statt_time = time.time()
 
    # save time of arrival
    while GPIO.input(echo) == 1:
        stop_time = time.time()
 
    # time difference between start and arrival
    time_elapsed = stop_time - statt_time

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (time_elapsed * 34300) / 2
 
    return distance

	 
if __name__ == '__main__':

    try:

		# set up the pins

		#GPIO Mode (BOARD / BCM)
		GPIO.setmode(GPIO.BCM)
 
		#set GPIO Pins
		GPIO_TRIGGER = 18
		GPIO_ECHO = 24
		 
		#set GPIO direction (IN / OUT)
		GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
		GPIO.setup(GPIO_ECHO, GPIO.IN)
		
        while True:
            dist = distance(trigger=GPIO_TRIGGER, echo=GPIO_ECHO)
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
