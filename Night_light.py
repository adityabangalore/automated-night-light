#Created By: Aditya Bangalore
#Date: July 4, 2020
#This code was uploaded to the Raspberry Pi to run the automatic light.

import RPi.GPIO as gpio		#import the Raspberry Pi GPIO library
import time			#import the time library

light = 3			#declare a variable for the light/relay (pin 3)
ts = 11				#declare a variable for the touch sensor (pin 11)

gpio.setmode(gpio.BOARD)	#tell the RPi to read the pins in the BOARD mode
gpio.setup(light, gpio.OUT)	#declare the light/relay as an output
gpio.setup(ts, gpio.IN)		#declare the touch sensor as an input

def buttonpush():		#declare a function responsible for toggling the touch sensor
	read_old = True		#declare an "old reading" as True
	light_state = False	#set the initial light state as False

	while True:
		t = time.asctime()	#store data about the local time in a variable called t
		hour = int(t[11:13])	#set the hour of the time as the 11th through 13th char of the t var
		minute = int(t[14:16])	#set the minute of the time as the 14th through 16th char of the t var
		second = int(t[17:19])	#set the second of the time as the 17th through 19th char of the t var
		
		read_new = gpio.input(ts)	#tell the RPi to read the sensor in a var called read_new
		
		if read_old == False and read_new == True:	#if the old reading is False and the new reading is True (the sensor has been pressed)...
			if light_state == False:		#if the light is off...
				gpio.output(light, True)	#turn the light on
				light_state = True		#set the light_state variable to True
			else:
				gpio.output(light, False)	#turn the light off
				light_state = False		#set the light_state variable to False
		elif hour == 1 and minute < 1 and second > 1:	#if it just passed 1 AM...
			break
		elif hour == 21 and minute < 1 and second < 1:	#if it just became 9 PM...
			break
	read_old = read_new	#set the old reading as the new reading for the new loop

def nightlight():	#declare a function responsible for automating the light
	while True:
		t = time.asctime()	#declare the necessary time variables
		hour = int(t[11:13])
		minute = int(t[14:16])
		second = int(t[17:19])

	if hour == 1 and minute < 1 and second < 1:	#if it just passed 1 AM...
		gpio.output(light, False)	#turn the light off
	elif hour == 21 and minute < 1 and second < 1:	#if it just became 9 AM...
		gpio.output(light, True)	#turn the light on
	else:
		buttonpush()

nightlight()	#run the nightlight() function
	
		
				
				
			