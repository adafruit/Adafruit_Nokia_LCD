# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import math
import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black hardware SPI config:
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

# Create drawing object.
draw = ImageDraw.Draw(image)

# Define text and get total width.
text = 'NOKIA 5110: NOT JUST FOR SNAKE ANYMORE. THIS IS AN OLD SCHOOL DEMO SCROLLER!! GREETZ TO: LADYADA & THE ADAFRUIT CREW, TRIXTER, FUTURE CREW, AND FARBRAUSCH'
maxwidth, height = draw.textsize(text, font=font)

# Set starting position.
startpos = 83
pos = startpos

# Animate text moving in sine wave.
print 'Press Ctrl-C to quit.'
while True:
	# Clear image buffer.
	draw.rectangle((0,0,83,47), outline=255, fill=255)
	# Enumerate characters and draw them offset vertically based on a sine wave.
	x = pos
	for i, c in enumerate(text):
		# Stop drawing if off the right side of screen.
		if x > 83:
			break
		# Calculate width but skip drawing if off the left side of screen.
		if x < -10:
			width, height = draw.textsize(c, font=font)
			x += width
			continue
		# Calculate offset from sine wave.
		y = (24-8)+math.floor(10.0*math.sin(x/83.0*2.0*math.pi))
		# Draw text.
		draw.text((x, y), c, font=font, fill=0)
		# Increment x position based on chacacter width.
		width, height = draw.textsize(c, font=font)
		x += width
	# Draw the image buffer.
	disp.image(image)
	disp.display()
	# Move position for next frame.
	pos -= 2
	# Start over if text has scrolled completely off left side of screen.
	if pos < -maxwidth:
		pos = startpos
	# Pause briefly before drawing next frame.
	time.sleep(0.1)
