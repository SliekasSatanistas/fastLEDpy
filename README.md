# fastLEDpy
There are great library for arduino fastLED - https://github.com/FastLED/FastLED
This library allow easily control addressable leds.

I wuold like to have such posibility to control led with RaspberyPy. For this purpose i will use python language. 
So, i will try to rewrite main maths/controls functions in Python.

For testing FastLed into grafichs (image file) it is neaded to instal library numpy:
https://sourceforge.net/projects/numpy/files/NumPy/
How to instal this library, read "readme".
but for the las time i was neaded to run these commands:

sudo apt-get install python-setuptools

sudo apt-get install python-dev

python setup.py build -j 4 install --prefix $HOME/.local
