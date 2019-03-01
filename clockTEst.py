#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# MAX7219-LED-4x8x8-Matrix digital clock By Lovisolo Pier Maurizio - Italy

import re
import time
import argparse
import locale
import datetime

# NOTE: change the following according to your locale setting
locale.setlocale(locale.LC_ALL,'it_IT.UTF-8')

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from itertools import repeat

def demo(n, block_orientation, rotate):
    # create device for linear preassembled 4x8x8 max7219 matrix
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90)
    device.contrast(0x05)
    print("Created device")
    # note: change device.contrast value (0xXX) to change leds brightness

    # start scrolling text demo - just once at startup
    msg = "DIGITAL CLOCK by Lovisolo Pier Maurizio - 2018"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)

    # MAX7219 4x8x8 LED Matrix Clock
    for _ in repeat(None):
     time.sleep(1)
     msg = time.asctime()
     msg= time.strftime("%H%M")
     with canvas(device) as draw:
      text(draw, (1, 0), msg, fill="white")
    time.sleep(1)
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate)
    except KeyboardInterrupt:
        pass