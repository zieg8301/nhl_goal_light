#!/usr/bin/env python

#test
from datetime import datetime
import time, os, random
import RPi.GPIO as GPIO
import subprocess, ctypes

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Tell the program you want to use pin number 15 as the input and pin 7 as output
GPIO.setup(15, GPIO.IN)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)

def activate_goal_light():
	#select random audio clip
	songrandom=random.randint(1, 3)
	#Set pin 7 output at high for goal light
	GPIO.output(7,False)
	#Play sound
	if (songrandom == 1):
		os.system("sudo mpg123 ./goal_horn_1.mp3")
	elif (songrandom == 2):
		os.system("sudo mpg123 ./goal_horn_2.mp3")
	elif (songrandom == 3):
		os.system("sudo mpg123 ./goal_horn_3.mp3")
	#Set pin 7 output at high for goal light
	GPIO.output(7,True)

def fetch_score():
	score=subprocess.check_output("wget -O- http://canadiens.nhl.com/gamecenter/en -nv | grep -o 'team.>MTL.*tot...' | grep -o 'tot.>.' | grep -o '[0-9]' | head -n 1", shell=True)
	return score

def score_int(score):
    	try:
		score=int(score)
    	except:
	    	pass
    	return score

def check_season():
	now = datetime.now()
	while now.month in (7, 8, 9):
            if now.day < 30 and now.month < 9:
		time.sleep(8640)
		now = datetime.datetime.now()
	while now.hour < 11:
		if now.minute < 30 :
            		time.sleep(900)
            		now = datetime.datetime.now()


#MAIN

#init        	
old_score=0
new_score=0
old_score=fetch_score()
old_score=score_int(old_score)


print ("When a goal is scored, please press the GOAL button...")
try:
	while (1):
	
		check_season()
		#check the state of the button/site two times per second
		time.sleep(0.5)
		
		#Check score online and save score
		new_score=fetch_score()
		#Convert string to integer
	    
		new_score=score_int(new_score)	
	
	
		#If new game, replace old score with 0
		if old_score > new_score:
			old_score=0
			
		#If score change...
		if new_score > old_score:
			#save new score
			old_score=new_score
			activate_goal_light()
	
		#If the button is pressed
		if(GPIO.input(15)==0):
			#save new score
			old_score=new_score
			activate_goal_light()

except KeyboardInterrupt:					
	#Restore GPIO to default state
	GPIO.cleanup()
	print ("'\nGPIO cleaned! Goodbye!")
