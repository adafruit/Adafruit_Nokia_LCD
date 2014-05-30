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

import unittest

from mock import Mock, call

import Adafruit_GPIO.SPI as SPI
import Adafruit_Nokia_LCD as LCD


class TestPCD8544(unittest.TestCase):
	def test_command_sets_dc_low(self):
		gpio = Mock()
		spi = Mock()
		lcd = LCD.PCD8544(1, 2, gpio=gpio, spi=spi)
		lcd.command(0xDE)
		gpio.set_low.assert_called_with(1)
		spi.write.assert_called_with([0xDE])

	def test_data_sets_dc_high(self):
		gpio = Mock()
		spi = Mock()
		lcd = LCD.PCD8544(1, 2, gpio=gpio, spi=spi)
		lcd.data(0xDE)
		gpio.set_high.assert_called_with(1)
		spi.write.assert_called_with([0xDE])

	def test_default_to_bitbang_spi(self):
		gpio = Mock()
		lcd = LCD.PCD8544(1, 2, 3, 4, 5, gpio=gpio)
		lcd.begin()
		self.assertIsInstance(lcd._spi, SPI.BitBang)

	def test_begin_initializes_lcd(self):
		gpio = Mock()
		spi = Mock()
		lcd = LCD.PCD8544(1, 2, gpio=gpio, spi=spi)
		lcd.begin(40)
		# Verify RST is set low then high.
		gpio.assert_has_calls([call.set_low(2), call.set_high(2)])
		# Verify SPI calls.
		spi.assert_has_calls([call.write([0x21]), 
							  call.write([0x14]),
							  call.write([0xA8]),
							  call.write([0x20]),
							  call.write([0x0c])])
