# TinkurBooth

Created by Adam Zolyak and Matthew Gorbsky
Tinkurlab
www.TinkurLab.com

Python 3.5.x

## Setup

1. Download [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) image
1. Flash image to a SD card using [Etcher](https://www.balena.io/etcher/)
1. Connect to monitor, keyboard, mouse, Ethernet and power up
1. Configure for local timezone, US Keyboard
1. Run `raspi-config` and enable the camera
1. Update Pi `using sudo apt-get update` and `sudo apt-get dist-upgrade`
1. Run `sudo apt-get install graphicsmagick`
1. Run `pip3 install RPi.GPIO`
1. Run `pip3 install python-dotenv`
1. Run `pip3 install luma.led_matrix`
1. Run `sudo apt-get install sshpass`
1. [Update GPU memory](https://raspberrypi.stackexchange.com/questions/13764/what-causes-enospc-error-when-using-the-raspberry-pi-camera-module) to `144`
1. Create a `.env` filr with the following variables:

```
PHOTO_FRAMES=4
FLOWDOCK_TOKEN=123456
FLOWDOCK_ORG=123456
FLOWDOCK_FLOW=123456
PRINTER_NAME_OR_IP=192.168.1.1
PRINTER_USER=john
PRINTER_PASSWORD=doe
```

Get Flowdock token from [https://flowdock.com/account/tokens](https://flowdock.com/account/tokens).
