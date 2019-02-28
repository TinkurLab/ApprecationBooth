# Unit: Push Photos from Pi to Mac and print

## Overview

1. Generate the print ready image file on the Pi and and save to Pi
1. Run scp with sshpass to transfer a file from the Pi to the Mac using `sshpass -p 'password' -v scp 1.txt zolad01@192.168.1.20:/Users/zolad01/Documents/Source/TinkurBooth/1_trans.txt`
1. Run `unit_print.py` on Mac. When new files are found on the Mac, the program sends them to the printer to print as 2x 2"x3" strips.

## To Do

- use host names not IPs

# Prerequisites

1. [Enable](https://www.maciverse.com/how-to-turn-on-your-macs-sftp.html) ssh / sftp / scp on Mac; optionally create a new service account for the transfers
1. Install sshpass on Pi `sudo apt-get install sshpass`

## Why this approach?

- Less complexity - computer to computer w/o third party internet services
- Fast - needs to be fast so the photo is printed almost immediatly; services such as Zapier and Google Drive take 5min - 15mins to sync / run
