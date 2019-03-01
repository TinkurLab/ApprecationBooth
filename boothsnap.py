#!/usr/bin/env python

#import for photo capture
import subprocess
import time
from time import sleep

#import for motion sensor
import RPi.GPIO as io

#import for email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os

# import for LED Matrix
#import max7219.led as led

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from itertools import repeat

#import for clock
import argparse
import locale
import datetime



####################################
#photo capture config
fps = .1  #delay between photos
total_dur = 4  #number of photos to be taken

#motion sensor config
button = 18

# GPIO setup
io.setmode(io.BOARD)
io.setup(button, io.IN, pull_up_down=io.PUD_UP)

#email config
USERNAME = "your@emailaddress.com"
PASSWORD = "yourpassword"

locale.setlocale(locale.LC_ALL, '') #use system time
####################################


### Initialize LED Matrix
# create device for linear preassembled 4x8x8 max7219 matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)
device.contrast(0x05)
print("Created device LED Matrix device")
# note: change device.contrast value (0xXX) to change leds brightness

#TODO GET THE IP ADDRESS AND DISPLAY ON THE MATRIX SO WE DON'T LOSE ACCESS


print("booth starting up...")

def displayScroll(msg):
	print(msg)
	show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.03)

def displayStatic(msg):
	print(msg)
	with canvas(device) as draw:
		text(draw, (1, 0), msg, fill="white", font=proportional(LCD_FONT))

def capture():
	#photo capture
	for x in range(total_dur):
		file_name = str(x) + '.jpg'
		# print "Taking photo in 3...2...1"
		# sleep (1)
		# print "Taking photo in 2..."
		# sleep (1)
		# print "Taking photo in 1..."
		# sleep (1)
		photoCount = x + 1
		displayScroll('Photo # ' + str(photoCount) + ' in 3')
		displayScroll('2')
		displayScroll('1')
		displayStatic('Hold!')
		subprocess.call (["raspistill", "-o", file_name, "-n", "-w", "800", "-h", "600"])
		print file_name
		sleep (fps)
	
	#print "processing photos"

	displayScroll('Sending to Cylons')

	graphicsmagick = "gm convert -delay 100 ~/Documents/src/TinkurBooth/*.jpg ~/Documents/src/TinkurBooth/ff.gif" 
	os.system(graphicsmagick)
	
	#print "uploading photos"

	displayScroll ('Thank you!')

### MAIN PROGRAM ###
def run():
	io.add_event_detect(button, io.FALLING)  # add falling edge detection on a channel
	sleep(1)
	
	while True:
		#io.wait_for_edge(button, io.FALLING)
		#print("Someone pushed the button!")
		
		if io.event_detected(button):
			print('Button pressed')
			## Button pressed, take photos
			capture()
			print "done - ready for button press"

		#Show clock while waiting
		print ('waiting...')
		time.sleep(1)
     	msg = time.asctime()
     	msg= time.strftime("%H%M")
     	displayStatic(msg)
    	time.sleep(1)
		
try:
	displayScroll('Ready')
	run()
except KeyboardInterrupt:
	pass
