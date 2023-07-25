#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
print("start")
pins = [12,16,20,21]

sequence = [[1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [1,0,0,1]]

def step(degrees, direction):
	steps = (int)(degrees * 512 / 360)

	for i in range(steps):
		for step in sequence:
			if (direction):
			
				GPIO.output(pins[0], step[0])
				GPIO.output(pins[1], step[1])
				GPIO.output(pins[2], step[2])
				GPIO.output(pins[3], step[3])
				time.sleep(0.001)
			else:
				GPIO.output(pins[0], step[0])
				GPIO.output(pins[3], step[3])
				GPIO.output(pins[2], step[2])
				GPIO.output(pins[1], step[1])

step(360,True)

GPIO.cleanup()

