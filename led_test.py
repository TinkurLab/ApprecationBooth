import max7219.led as led

device = led.matrix(cascaded = 4)
device.show_message("Hello world!")