#!/usr/bin/python
#
# wiitrakPICON.py
# Connect a Nintendo Wii Remote via Bluetooth
# and  read the button states in Python.
# using PiZero and Picon Zero board
#
# Matthew Parry 2013 & 2017 (piConZero extensions)
#
# Based on code by Matt Hawkins (raspberryspy)

# -----------------------
# Import required Python libraries
# -----------------------
import cwiid		#module for connecting Wii remote
import time
import os
import RPi.GPIO as GPIO
import piconzero as pz
import hcsr04                      #module for hcsr04 ultrasonic sensor
import threewaylinetracker as line #module for ryantek 3 way line tracker

speed = 100    #speed of motors (any lower and get whine)
button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN

while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    pz.stop()   #stop motors
    exit(wii)

  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    pz.spinLeft(speed)
    time.sleep(0.25)
    pz.stop()
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    pz.spinRight(speed)
    time.sleep(0.25)
    pz.stop()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    pz.forward(speed)
    time.sleep(0.25)
    pz.stop()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    pz.reverse(speed)
    time.sleep(0.25)
    pz.stop()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed - stop motors'
    pz.stop()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed - start auto drive'
    #go forwards unless obstacle
    autoDrive = True
    hcsr04.init()
    distance = int(hcsr04.getDistance())
    print distance

    while autoDrive:
      if distance > 5 and autoDrive:
        pz.forward(speed)
        time.sleep(button_delay)
        distance = int(hcsr04.getDistance())
        if wii.state['buttons'] & cwiid.BTN_1:
          autoDrive = False
        print distance
    #5 cm off so reverse a bit
      else:
        pz.reverse(speed)
        print "reverse a bit"
        time.sleep(0.25)
        pz.spinLeft(speed)
        print "left a bit"
        time.sleep(0.25)
        pz.stop()
        distance = int(hcsr04.getDistance())
        print "stop"
        time.sleep(button_delay)
    #if button 1 pressed then stop
    pz.stop()
    hcsr04.cleanup()
    time.sleep(button_delay)
    

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed - start line tracking'
    line.init()
    lineTrack = True
    #do line tracking
    while lineTrack:

      line_left = int(line.getLeft())
      line_right = int(line.getRight())

      if line_left == 0:
        #drive to right
        print "right"
        pz.spinRight(speed)
        time.sleep(0.25)
        #then go forward
        pz.forward(speed)
        time.sleep(0.25)
      elif line_right == 0:
        #drive left
        print "left"
        pz.spinLeft(speed)
        time.sleep(0.25)
        #then go forward
        pz.forward(speed)
        time.sleep(0.25)
      else:
        #just go forwards
        print "forwards"
        pz.forward(speed)
        time.sleep(0.25)

      if wii.state['buttons'] & cwiid.BTN_1:
        lineTrack = False

    #if button 1 pressed then stop
    pz.stop()
    line.cleanup()          
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed - lights on'
    speed = 0.2
    pz.setOutputConfig(0, 1)    
    lights = True
    while lights:
        pz.setOutput(0, 5) # 5% very dim
        time.sleep(speed)
        if wii.state['buttons'] & cwiid.BTN_B:
          lights = False
        pz.setOutput(0, 30) # 30% medium
        time.sleep(speed)
        if wii.state['buttons'] & cwiid.BTN_B:
          lights = False
        pz.setOutput(0, 70) # 70% bright
        time.sleep(speed)
        if wii.state['buttons'] & cwiid.BTN_B:
          lights = False
        pz.setOutput(0, 100) # 100% maximum
        time.sleep(speed)
        if wii.state['buttons'] & cwiid.BTN_B:
          lights = False
        pz.setOutput(0, 70) # 70% bright
        time.sleep(speed)
        if wii.state['buttons'] & cwiid.BTN_B:
          lights = False
        pz.setOutput(0, 30) # 30% medium
        time.sleep(speed)

    pz.setOutput(0,0)  #lights off
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
