from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'Adafruit_Nokia_LCD',
	  version 			= '0.1.0',
	  author			= 'Tony DiCola',
	  author_email		= 'tdicola@adafruit.com',
	  description		= 'Library to display images on the Nokia 5110/3110 LCD.',
	  license			= 'MIT',
	  url				= 'https://github.com/adafruit/Adafruit_Nokia_LCD/',
	  packages 			= find_packages())
