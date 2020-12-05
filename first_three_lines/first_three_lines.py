#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: A-Pot 
# https://github.com/A-Pot/pot-pi

# Description: Get started with just 3 lines of code!
# Date: November 22, 2020

from gpiozero import LED
myLED = LED(21)
myLED.toggle()
