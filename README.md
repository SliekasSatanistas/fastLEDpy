# fastLEDpy
There are great library for arduino fastLED - https://github.com/FastLED/FastLED
This library allow easily control addressable leds.

I wuold like to have such posibility to control led with RaspberyPy. For this purpose i will use python language. 
So, i will try to rewrite main maths/controls functions in Python.

For testing FastLed into grafichs (image file) is used python PIL library, which, i think, usualy is installed by default.

it is required Neopixel library for python (https://learn.adafruit.com/neopixels-on-raspberry-pi/software)
0. sudo apt-get install python-pip
0. sudo apt-get install build-essential python-dev git scons swig
1. Download sources from: git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install

