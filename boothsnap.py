#!/usr/bin/env python

# import for .env variables
import os
from dotenv import load_dotenv

# import for photo capture
import subprocess
import time
from time import sleep

# import for GPIO sensor
import RPi.GPIO as io

# import for LED Matrix
#import max7219.led as led

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from itertools import repeat

# import for clock
import argparse
import locale
import datetime
import re

# import for IP adress
import socket
import fcntl
import struct

# load .env variables
load_dotenv(dotenv_path='.env', verbose=True)


def get_ip_address():
    ip_address = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


# print get_ip_address('lo')
ip = get_ip_address()
print(ip)

####################################
# photo capture config
fps = .1  # delay between photos
total_dur = int(os.getenv("PHOTO_FRAMES"))  # number of photos to be taken

# button config
button = 18

# GPIO setup
io.setmode(io.BOARD)
io.setup(button, io.IN, pull_up_down=io.PUD_UP)

locale.setlocale(locale.LC_ALL, '')  # use system time
####################################


# Initialize LED Matrix
# create device for linear preassembled 4x8x8 max7219 matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)
device.contrast(0x05)
print("Created device LED Matrix device")
# note: change device.contrast value (0xXX) to change leds brightness

# TODO GET THE IP ADDRESS AND DISPLAY ON THE MATRIX SO WE DON'T LOSE ACCESS


print("booth starting up...")


def displayScroll(msg):
    # print(msg)
    show_message(device, msg, fill="white",
                 font=proportional(LCD_FONT), scroll_delay=0.03)


def displayStatic(msg):
    # print(msg)
    with canvas(device) as draw:
        text(draw, (1, 0), msg, fill="white", font=proportional(LCD_FONT))


def capture():
    # photo capture
    for x in range(total_dur):
        file_name = str(x) + '.jpg'
        # sleep (1)
        # print "Taking photo in 2..."
        # sleep (1)
        # print "Taking photo in 1..."
        # sleep (1)
        photoCount = x + 1
        print("Taking photo " + str(photoCount))
        displayScroll('Photo # ' + str(photoCount) + ' in 3')
        displayScroll('2')
        displayScroll('1')
        displayStatic('Hold!')
        subprocess.call(["raspistill", "-o", file_name,
                         "-n", "-w", "800", "-h", "600"])
        print(file_name)
        sleep(fps)

    # print "processing photos"

    displayScroll('Sending to Cylons')

    graphicsmagick = "gm convert -delay 100 ~/Documents/src/TinkurBooth/*.jpg ~/Documents/src/TinkurBooth/ff.gif"
    os.system(graphicsmagick)

    # print "uploading photos"

    displayScroll('Thank you!')

    return "ff.gif"


def postToFlowdock():
    filename = 'ff.gif'
    flowdockToken = os.getenv("FLOWDOCK_TOKEN")
    flowdockOrg = os.getenv("FLOWDOCK_ORG")
    flowdockFlow = os.getenv("FLOWDOCK_FLOW")
    flowdockCurl = 'curl -v -X POST -F "event=file" -F "content=@%s" https://%s@api.flowdock.com/flows/%s/%s/messages' % (
        filename, flowdockToken, flowdockOrg, flowdockFlow)

    print("Posting to Flowdock...")
    os.system(flowdockCurl)


def printPhoto():
    filename = '0.jpg'
    printerUser = os.getenv("PRINTER_USER")
    printerPassword = os.getenv("PRINTER_PASSWORD")
    printerTransfer = 'sshpass -p %s -v scp %s %s@192.168.1.32:/Users/pi/Documents/Source/TinkurBooth/%s' % (
        printerPassword, filename, printerUser, filename)

    print("Transfering photo to printer...")
    os.system(printerTransfer)


### MAIN PROGRAM ###


def run():
    # add falling edge detection on a channel
    io.add_event_detect(button, io.FALLING)
    print('listening for button press')
    sleep(1)

    while True:
        #io.wait_for_edge(button, io.FALLING)
        #print("Someone pushed the button!")

        if io.event_detected(button):
            print('Button pressed')
            # Button pressed, take photos
            capture()
            postToFlowdock()
            printPhoto()
            print("done - ready for button press")

        #print ('waiting...')
        time.sleep(1)
        displayScroll('.')
        # print('waiting...')
    # displayScroll('waiting')


try:
    displayScroll('Ready')
    displayScroll(str(ip))
    run()
except KeyboardInterrupt:
    pass
