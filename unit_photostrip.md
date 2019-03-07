## Unit Print Formatted Photo

## Overview

Using imagemagick to manipulate images from a terminal. These can be used to create a composed photo (ex. photo strip) for printing.

## Documentation

https://imagemagick.org/script/command-line-processing.php

## Examples

### Crop an Image\*\*

`magick 0.jpg -crop '690x460+50+130' crop.jpg`

crop an image to 690x460 starting at x50 and y130 and save to crop.jpg

### Montage Multiple Images Together

`montage header.png crop.jpg whitebox.png -tile 1x3 -geometry +50+50 final.jpg`

montage multiple images in a 1 horizonal x 3 vertical arrangement, adding a x50 by y50 border and save to final.jpg

## Debugging

The following example creates a negative image using geometry coordinates and is a good way to debug geometry coordinates:
`magick test5.jpg -region '1200x800+150+200' -negate crop.jpg`
