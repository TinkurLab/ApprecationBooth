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
	print(io.input(pir_pin))
    sleep(1)