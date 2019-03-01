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

# LED Matrix imports
#import max7219.led as led

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from itertools import repeat


####################################
#photo capture config
fps = 1  #delay between photos
total_dur = 4  #number of photos to be taken

#motion sensor config
pir_pin = 18

# GPIO setup
io.setmode(io.BOARD)
io.setup(pir_pin, io.IN, pull_up_down=io.PUD_UP)

#email config
USERNAME = "your@emailaddress.com"
PASSWORD = "yourpassword"
####################################


### Initialize LED Matrix
# create device for linear preassembled 4x8x8 max7219 matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)
device.contrast(0x05)
print("Created device LED Matrix device")
# note: change device.contrast value (0xXX) to change leds brightness

# start scrolling text demo - just once at startup
msg = "4Frames Starting Up"
print(msg)
show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)


print("booth starting up...")


def run
	while True:
		io.wait_for_edge(pir_pin, io.FALLING)
		print("PIR ALARM!")
		
		#photo capture
		for x in range(total_dur):
			file_name = str(x) + '.jpg'
			print "Taking photo in 3..."
			sleep (1)
			print "Taking photo in 2..."
			sleep (1)
			print "Taking photo in 1..."
			sleep (1)
			subprocess.call (["raspistill", "-o", file_name, "-n", "-w", "600", "-h", "450"])
			print file_name
			sleep (fps)
		
		print "processing photos"

		graphicsmagick = "gm convert -delay 100 ~/Documents/src/TinkurBooth/*.jpg ~/Documents/src/TinkurBooth/ff.gif" 
		os.system(graphicsmagick)
		
		print "uploading photos"

		

		#send email
		# def sendMail(to, subject, text, files=[]):
		# 	assert type(to)==list
		# 	assert type(files)==list
		
		# 	msg = MIMEMultipart()
		# 	msg['From'] = USERNAME
		# 	msg['To'] = COMMASPACE.join(to)
		# 	msg['Date'] = formatdate(localtime=True)
		# 	msg['Subject'] = subject
			
		# 	msg.attach( MIMEText(text) )
		
		# 	for file in files:
		# 		part = MIMEBase('application', "octet-stream")
		# 		part.set_payload( open(file,"rb").read() )
		# 		Encoders.encode_base64(part)
		# 		part.add_header('Content-Disposition', 'attachment; filename="%s"'
		# 						% os.path.basename(file))
		# 		msg.attach(part)
		
		# 	server = smtplib.SMTP('smtp.gmail.com:587')
		# 	server.ehlo_or_helo_if_needed()
		# 	server.starttls()
		# 	server.ehlo_or_helo_if_needed()
		# 	server.login(USERNAME,PASSWORD)
		# 	server.sendmail(USERNAME, to, msg.as_string())
		# 	server.quit()
		
		# sendMail( ["sender@youremail.com"],
		# 		"Email Subject Goes Here",
		# 		"Email Body Goes Here",
		# 	["ff.gif"])


		print "done - ready to shoot"

		time.sleep(1.0)

try:
	run()
except KeyboardInterrupt:
	pass
