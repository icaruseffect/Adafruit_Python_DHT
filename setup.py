from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages, Extension
import sys

# Pick the right extension to compile based on the platform.
extensions = []
extensions.append(Extension("Adafruit_DHT.WiringX_Driver",
							["source/_WiringX_Driver.c", "source/common_dht_read.c", "source/WiringX/wiringx_dht_read.c"],
							libraries=['rt', 'wiringX'],
							extra_compile_args=['-std=gnu99']))

# Call setuptools setup function to install package.
setup(name              = 'Adafruit_DHT',
	  version           = '1.1.0',
	  author            = 'Tony DiCola',
	  author_email      = 'tdicola@adafruit.com',
	  description       = 'Library to get readings from the DHT11, DHT22, and AM2302 humidity and temperature sensors using WiringX library.',
	  license           = 'MIT',
	  url               = 'https://github.com/adafruit/Adafruit_Python_DHT/',
	  packages          = find_packages(),
	  ext_modules       = extensions)
