#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import numpy as np
import time
import random
import serial
import sys
from random import randrange
import subprocess
import os
import threading

device = raw_input("Please enter device: ")
print "you entered ", device

#conectarse al arduino en el puerto que corresponda
print "Trying to connect, using 9600..."
arduino = serial.Serial(device, 9600,timeout=2)

while(True):
    valor = arduino.readline()
    print (valor)
