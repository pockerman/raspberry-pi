import spidev
import time

def read_analog(chan, spi):
     r = spi.xfer2([1, (8 + chan) << 4, 0])    
     adc_out = ((r[1]&3) << 8) + r[2]
     return adc_out
     
def main(spi):
    while True:
       reading = read_analog(chan=0, spi=spi)    
       voltage = reading * 3.3 / 1024    
       temp_c = voltage * 100 - 50    
       temp_f = temp_c * 9.0 / 5.0 + 32
       print("Temp C=%f\t\tTemp f=%f" % (temp_c, temp_f))    
       time.sleep(1)


if __name__ == '__main__':

    # set up the channel
    spi = spidev.SpiDev()
    spi.open(0,0)
    main(spi)

