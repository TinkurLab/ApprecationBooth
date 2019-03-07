# Python: 2.7.x

# More Info
#   * https://www.cups.org/doc/options.html?VERSION=1.7&Q=
#   * https://superuser.com/questions/681845/printing-via-commandline-cups-with-photo-printer

import os
import time
path_to_watch = "."  # "." is the current directory of this repo
before = dict([(f, None) for f in os.listdir(path_to_watch)])
print "Running"
while 1:
    time.sleep(5)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        for photo in added:
            print "Photo: " + photo
            os.system("lp -d HiTi_P510L -o fit-to-page -o media=P6x4 " + photo)
    before = after
