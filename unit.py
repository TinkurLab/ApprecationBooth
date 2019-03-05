import RPi.GPIO as GPIO
import time

pin = 21         # The pin connected to the LED
iterations = 10  # The number of times to blink
interval = 2   # The length of time to blink on or off

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

# The parameters to "range" are inclusive and exclusive, respectively,
#  so to go from 1 to 10 we have to use 1 and 11 (add 1 to the max)
for x in range(1, iterations+1):

    print("Loop %d: LED on" % (x))
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)

    print("Loop %d: LED off" % (x))
    GPIO.output(pin, GPIO.LOW)
    time.sleep(interval)
