#!/usr/bin/env python

#from datetime import datetime
from datetime import date
import time, os, random
import requests
#import requests_cache
import RPi.GPIO as GPIO
#from IPython import embed

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Tell the program you want to use pin number 15 as the input and pin 7 as output
GPIO.setup(15, GPIO.IN)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)

#requests_cache.install_cache()
#requests_cache.clear()

def activate_goal_light():
	#select random audio clip
	songrandom=random.randint(1, 3)
	#Set pin 7 output at high for goal light ON
	GPIO.output(7,False)
	#Play sound
	command_play_song='sudo mpg123 ./audio/goal_horn_{SongId}.mp3'.format(SongId=str(songrandom))
	os.system(command_play_song)
	#Set pin 7 output at high for goal light OFF
	GPIO.output(7,True)

def fetch_score():
	now=date.today()
        url='http://statsapi.web.nhl.com/api/v1/schedule?teamId=8&date={:%Y-%m-%d}'.format(now)
	score=requests.get(url)
	score=score.text[score.text.find("id\" : 8")-37:score.text.find("id\" : 8")-36]
	score=int(score)
	print score
	return score

def check_season():
	now = date.today()
	if now.month in (7, 8, 9):
            	return False
	else:
		return True

def check_if_game():
	#embed()
	now=date.today()
        url='http://statsapi.web.nhl.com/api/v1/schedule?teamId=8&date={:%Y-%m-%d}'.format(now)
        gameday_url=requests.get(url)
	if "gamePk" in gameday_url.text:
		return True
	else:
		return False

#MAIN

#init        	
old_score=0
new_score=0

gameday=False
season=False

print ("When a goal is scored, press the GOAL button...")
try:
	#team=raw_input("Enter team you want to setup goal light for (Default: CANADIENS) \n")
        #if team is "":
	#	team="CANADIENS"
	#team=team.upper()
	
	while (1):
		season=check_season() #check if in season
		#(game_id,team_abr)=check_if_game(team) #check if game tonight/need to update with today's date
		gameday=check_if_game()	
		
		if season:
			if gameday:
				#Check score online and save score
				new_score=fetch_score()
			    
				#If new game, replace old score with 0
				if old_score > new_score:
					old_score=0
			
				#If score change...
				if new_score > old_score:
					#save new score
					old_score=new_score
					activate_goal_light()
					print "GOAL!"
			
				#If the button is pressed
				if(GPIO.input(15)==0):
					#save new score
					old_score=new_score
					activate_goal_light()
			else:
				print "No Game Today!"
				now=date.today()
				time_to_sleep=timedelta(days=1)
				print time_to_sleep.total_seconds()
				#time.sleep(time_to_sleep)
		else:
			print "OFF SEASON!"
			now=now=datetime.now()
			time_to_sleep=(timedelta(weeks=3)-now).total_seconds()
			#time.sleep(time_to_sleep)
						
except KeyboardInterrupt:					
	#requests_cache.clear()
	#print "\nCache cleaned!"
	#Restore GPIO to default state
	GPIO.cleanup()
	print "GPIO cleaned! Goodbye!"
	
