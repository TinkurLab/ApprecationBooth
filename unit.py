import RPi.GPIO as GPIO
import time

ledPin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)

while True:
    print("LED on")
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(ledPin, GPIO.LOW)
