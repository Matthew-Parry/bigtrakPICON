#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BigTrak.py
#  
#  Copyright 2013  Matthew Parry
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
import RPi.GPIO as GPIO
import time

#Declare GPIO settings
PWMA = 7		#Pin for PWM for motor A
AIN2 = 11		#Pin for motor A control 2
AIN1 = 12		#Pin for motor A control 1
STBY = 13		#Pin for motor Standby
BIN1 = 15		#Pin for motor B control 1
BIN2 = 16		#Pin for motor B control 2
PWMB = 18		#Pin for PWM for motor B

LEDPIN = 22	##25

def setupPins(*ignore):
	#Function to set Raspberry pi board pins
	GPIO.setmode(GPIO.BOARD)

	# set up GPIO pins
	GPIO.setup(PWMA, GPIO.OUT)
	GPIO.setup(AIN2, GPIO.OUT)
	GPIO.setup(AIN1, GPIO.OUT)
	GPIO.setup(STBY, GPIO.OUT)
	GPIO.setup(BIN1, GPIO.OUT)
	GPIO.setup(BIN2, GPIO.OUT)
	GPIO.setup(PWMB, GPIO.OUT)
	GPIO.setup(LEDPIN, GPIO.OUT)

def goforwards(seconds):
	#Function to drive forwards for x seconds
	#Set AIN1/BIN1 = HIGH and AIN2/BIN2 = LOW
	#Set the direction of Motor A
	GPIO.output(AIN1, GPIO.HIGH) #Set AIN1
	GPIO.output(AIN2, GPIO.LOW) #Set AIN2
	#Set the Speed / PWM for A
	GPIO.output(PWMA, GPIO.HIGH) #Set PWMA
	
	GPIO.output(LEDPIN, GPIO.HIGH)	#Set LED

	#Set the direction of Motor B
	GPIO.output(BIN1, GPIO.HIGH)
	GPIO.output(BIN2, GPIO.LOW)
	#Set the Speed / PWM for B
	GPIO.output(PWMB, GPIO.HIGH)

	#Make sure STBY is disabled - Set it to HIGH
	GPIO.output(STBY, GPIO.HIGH)

	time.sleep(seconds)

def gobackwards(seconds):
	#Function to drive backwards for x seconds
	#Set AIN1/BIN1 = LOW and AIN2/BIN2 = HIGH
	#Set the direction of Motor A
	GPIO.output(AIN1, GPIO.LOW) 
	GPIO.output(AIN2, GPIO.HIGH) 
	#Set the Speed / PWM for A
	GPIO.output(PWMA, GPIO.HIGH) 

	#Set the direction of Motor B
	GPIO.output(BIN1, GPIO.LOW) 
	GPIO.output(BIN2, GPIO.HIGH) 
	#Set the Speed / PWM for B
	GPIO.output(PWMB, GPIO.HIGH) 

	#Make sure STBY is disabled - Set it to HIGH
	GPIO.output(STBY, GPIO.HIGH)

	time.sleep(seconds)
	
def goright(seconds):
	#Function to turn right for x seconds
	#Set AIN1/BIN2 = LOW and AIN2/BIN1 = HIGH
	#Set the direction of Motor A
	GPIO.output(AIN1, GPIO.LOW) 
	GPIO.output(AIN2, GPIO.HIGH) 
	#Set the Speed / PWM for A
	GPIO.output(PWMA, GPIO.HIGH) 

	#Set the direction of Motor B
	GPIO.output(BIN2, GPIO.LOW) 
	GPIO.output(BIN1, GPIO.HIGH) 
	#Set the Speed / PWM for B
	GPIO.output(PWMB, GPIO.HIGH) 

	#Make sure STBY is disabled - Set it to HIGH
	GPIO.output(STBY, GPIO.HIGH)

	time.sleep(seconds)

def goleft(seconds):
	#Function to turn left for x seconds
	#Set AIN2/BIN1 = LOW and AIN1/BIN2 = HIGH
	#Set the direction of Motor A
	GPIO.output(AIN2, GPIO.LOW) 
	GPIO.output(AIN1, GPIO.HIGH) 
	#Set the Speed / PWM for A
	GPIO.output(PWMA, GPIO.HIGH) 

	#Set the direction of Motor B
	GPIO.output(BIN1, GPIO.LOW) 
	GPIO.output(BIN2, GPIO.HIGH) 
	#Set the Speed / PWM for B
	GPIO.output(PWMB, GPIO.HIGH) 

	#Make sure STBY is disabled - Set it to HIGH
	GPIO.output(STBY, GPIO.HIGH)

	time.sleep(seconds)

def resetpins(*ignore):
	#Now set everything to low (Switch everything Off)
	GPIO.output(AIN1, GPIO.LOW) #Set AIN1
	GPIO.output(AIN2, GPIO.LOW) #Set AIN2
	GPIO.output(PWMA, GPIO.LOW) #Set PWMA
	GPIO.output(BIN1, GPIO.LOW) #Set BIN1
	GPIO.output(BIN2, GPIO.LOW) #Set BIN2
	GPIO.output(PWMA, GPIO.LOW) #Set PWMA
	GPIO.output(STBY, GPIO.LOW) #Set STBY
	
	GPIO.output(LEDPIN, GPIO.LOW)	#Set LED

	GPIO.cleanup()	#free all pins





