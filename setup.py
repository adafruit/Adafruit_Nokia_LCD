try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

setup(name                = 'Adafruit_Nokia_LCD',
      version             = '0.2.0',
      author              = 'Tony DiCola',
      author_email        = 'tdicola@adafruit.com',
      description         = 'Library to display images on the Nokia 5110/3110 LCD.',
      license             = 'MIT',
      url                 = 'https://github.com/adafruit/Adafruit_Nokia_LCD/',
      dependency_links    = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.1.0'],
      install_requires    = ['Adafruit-GPIO>=0.1.0'],
      packages            = find_packages())
