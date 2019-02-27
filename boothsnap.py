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

print("booth starting up...")

while True:
	io.wait_for_edge(pir_pin, io.FALLING)
	print("PIR ALARM!")
	
	#photo capture
	for x in range(total_dur):
		file_name = str(x) + '.jpg'
		print file_name
		subprocess.call (["raspistill", "-o", file_name, "-n", "-w", "600", "-h", "450"])
		sleep (fps)
	
	print "processing photos"

	graphicsmagick = "gm convert -delay 100 *.jpg ff.gif" 
	subprocess.call (graphicsmagick)
	
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
