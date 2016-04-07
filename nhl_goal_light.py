#!/usr/bin/env python

from datetime import timedelta
from datetime import datetime
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

def get_team():
	team=raw_input("Enter team you want to setup goal light for (Default: CANADIENS) \n")
        if team is "":
		team="Canadiens"
	team=team.title()
	url='http://statsapi.web.nhl.com/api/v1/teams'
	team_list=requests.get(url)
	team_list=team_list.text[team_list.text.find(team)-50:team_list.text.find(team)]
	print team_list
	teamID=team_list[team_list.find("id")+6:team_list.find("id")+8]
	print teamID
	return teamID

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

def fetch_score(teamID):
	now=datetime.now()
        url='http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date={:%Y-%m-%d}'.format(teamID,now)
	score=requests.get(url)
	score=score.text[score.text.find("id\" : {}".format(teamID))-37:score.text.find("id\" : {}".format(teamID))-36]
	score=int(score)
	print score now
	return score

def check_season():
	now = datetime.now()
	if now.month in (7, 8, 9):
            	return False
	else:
		return True

def check_if_game(teamID):
	#embed()
	now=datetime.now()
        url='http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date={:%Y-%m-%d}'.format(teamID,now)
        gameday_url=requests.get(url)
	if "gamePk" in gameday_url.text:
		return True
	else:
		return False
def sleep(sleep_period):
	now=datetime.now()
   	if "day" in sleep_period:
     		delta=timedelta(days=1)
	elif "season" in sleep_period:
		if now.month is 8:
			delta=timedelta(days=31)
		else:
			delta=timedelta(days=30)
    	next_day=datetime.today()+delta
    	next_day=next_day.replace(hour=0,minute=0)
    	sleep=next_day-now
    	sleep=sleep.total_seconds()
    	time.sleep(sleep)

#MAIN

#init        	
old_score=0
new_score=0

gameday=False
season=False

print ("When a goal is scored, press the GOAL button...")
try:
	teamID=get_team()
	while (1):
		season=check_season() #check if in season
		#(game_id,team_abr)=check_if_game(team) #check if game tonight/need to update with today's date
		gameday=check_if_game(teamID)	
		
		if season:
			if gameday:
				#Check score online and save score
				new_score=fetch_score(teamID)
			    
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
				sleep("day")
		else:
			print "OFF SEASON!"
			sleep("season")
						
except KeyboardInterrupt:					
	#requests_cache.clear()
	#print "\nCache cleaned!"
	#Restore GPIO to default state
	GPIO.cleanup()
	print "GPIO cleaned! Goodbye!"
	
