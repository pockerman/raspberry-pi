
# Code adapted from RasPi I2C Sensor - Beginning Sensor Networks 2nd Edition


import time
import board
import busio
import adafruit_bmp280

def main(bmp280):

	while True:

		try:
			p = float(bmp280.pressure)
			altitude = bmp280.altitude
			print("Pressure at {0:.3f}: {1:.3f}".format(p, altitude))
			time.sleep(3)
		except  KeyboardInterrupt:
			break


if __name__ == '__main__':
	i2c = busio.I2C(board.SCL, board.SDA)
	bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

	# calibarte sea level pressure
	bmp280.sea_level_pressure = 1013.25

	main(bmp280)



