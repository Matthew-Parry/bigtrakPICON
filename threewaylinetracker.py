#======================================================================
#
# Python Module to handle a 3 way line tracker (HY Studio sold by ryantec)
# Aimed at use on Picon Zero
#
# Created by Matthew Parry August 2017
# Based on code from MagPi 38 Oct 2015 (magpibot.py)
#
# This code is in the public domain and may be freely copied and used
# No warranty is provided or implied
#
#======================================================================

import RPi.GPIO as GPIO, sys, threading, time, os, subprocess


# Define GPIO pins
CENTRE = 13 #bcm 27
LEFT = 12 #bcm 18
RIGHT = 15 #bcm 22

#======================================================================
# General Functions
#
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def cleanup():
    GPIO.cleanup()

#======================================================================

#======================================================================
#
# getLeft(). display left reading only
def getLeft():
    GPIO.setup(LEFT, GPIO.IN)
    line_left = GPIO.input(LEFT)
#    print line_left
 #   print "left"

    return line_left
    
#
# getRight(). display right reading only
def getRight():
    GPIO.setup(RIGHT, GPIO.IN)
    line_right = GPIO.input(RIGHT)

    return line_right
    
#======================================================================

