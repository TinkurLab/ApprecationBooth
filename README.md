# TinkurBooth

Created by Adam Zolyak and Matthew Gorbsky
Tinkurlab
www.TinkurLab.com

Python 3.5.x

## Hardware

- Raspberry Pi [Model B+ v1.2](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) ([pinout](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2.jpg))
- Raspberry Pi Camera v1
- LCD Matrix
- Button
- Mac Laptop
- HiTi Dye Sublimation Photo Printer P510L

## Setup

1. Download [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) image
2. Flash image to a SD card using [Etcher](https://www.balena.io/etcher/)
3. Connect to monitor, keyboard, mouse, Ethernet and power up
4. Configure for local timezone, US Keyboard
5. Run `raspi-config` and enable the camera
6. Update Pi `using sudo apt-get update` and `sudo apt-get dist-upgrade`
7. Verify Python 3.5.x or > is installed by running `python3`; upgrade if needed
8. Run `sudo apt-get install graphicsmagick`
9. Run `pip3 install RPi.GPIO`
10. Run `pip3 install python-dotenv`
11. Run `pip3 install luma.led_matrix`
12. Run `sudo apt-get install sshpass`
13. [Update GPU memory](https://raspberrypi.stackexchange.com/questions/13764/what-causes-enospc-error-when-using-the-raspberry-pi-camera-module) to `144`
14. Create a `.env` filr with the following variables:

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

15. Run `sudo raspi-config` and enable wait for network under boot options.
16. Run `sudo nano /etc/rc.local` with the following:

```
# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

# Start Photobooth
printf "Starting Photobooth"
cd /home/pi/Documents/src/TinkurBooth/
sudo -H -u pi /usr/bin/python3 boothsnap.py &
exit 0
```

17. To verify script is starting when the Pi boots, run `systemctl status rc.local.service` to view the `rc.local` startup logs.

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

## Broadcom Chips

BCM2837 Quad Core 1.2GHz Broadcom 64bit CPU
BCM43438 wireless LAN and Bluetooth Low Energy (BLE) on board
MMAL (Multimedia Abstraction Layer) is a C library designed by Broadcom for use with the Videocore IV GPU found on the Raspberry Pi.
