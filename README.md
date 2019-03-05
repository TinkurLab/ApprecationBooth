# TinkurBooth

Created by Adam Zolyak and Matthew Gorbsky
Tinkurlab
www.TinkurLab.com

Python 3.5.x

## Hardware

- Raspberry Pi Model B+ v2 ([pinout](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2.jpg))
- Raspberry Pi Camera v1
- LCD Matrix
- Button
- Mac Laptop
- HiTi Dye Sublimation Photo Printer P510L

## Setup

1. Download [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) image
1. Flash image to a SD card using [Etcher](https://www.balena.io/etcher/)
1. Connect to monitor, keyboard, mouse, Ethernet and power up
1. Configure for local timezone, US Keyboard
1. Run `raspi-config` and enable the camera
1. Update Pi `using sudo apt-get update` and `sudo apt-get dist-upgrade`
1. Verify Python 3.5.x or > is installed by running `python3`; upgrade if needed
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

Obtain Flowdock token from [https://flowdock.com/account/tokens](https://flowdock.com/account/tokens).

## Wiring

### LCD Display

| LCD Pin | Raspberry Pi Pin |
| ------- | ---------------- |
| VCC     | 5v               |
| GND     | GND              |
| DIN     | MOSI             |
| CS      | CE0              |
| CLK     | SCK              |

### Button

| Button Pin                       | Raspberry Pi Pin     |
| -------------------------------- | -------------------- |
| Button (polarity doesn't matter) | GPIO24               |
| Button (polarity doesn't matter) | GND                  |
| LED +                            | GPIO21               |
| LED GND                          | 220Ω resistor to GND |
