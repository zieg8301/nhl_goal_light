#!/usr/bin/env python

from datetime import datetime
import time, os, random
import requests
import RPi.GPIO as GPIO
#from IPython import embed

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Tell the program you want to use pin number 15 as the input and pin 7 as output
GPIO.setup(15, GPIO.IN)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)

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

def fetch_score(game_id,team_abr):
	season_id = game_id[:4] + str(int(game_id[:4])+1)
	url='http://live.nhle.com/GameData/{Season}/{GameId}/gc/gcbx.jsonp'.format(Season=season_id,GameId=game_id)
        score=requests.get(url)
	score=score.text[score.text.find("goalSummary"):]
	score=score.count('t1":"{team_abr}'.format(team_abr=team_abr))
	print score
	return score

def check_season():
	now = datetime.now()
	while now.month in (7, 8, 9):
            if now.day < 23 and now.month < 9:
            	print "OFF SEASON!"
		time.sleep(604800)
		now = datetime.datetime.now()

def check_if_game(team):
	#embed()
	now=datetime.now()
        url='http://live.nhle.com/GameData/GCScoreboard/{:%Y-%m-%d}.jsonp'.format(now)
        MTL=requests.get(url)
	while team not in MTL.text:
		print "No game today!"
		time.sleep(43200)
		now=datetime.now()
        	url='http://live.nhle.com/GameData/GCScoreboard/{:%Y-%m-%d}.jsonp'.format(now)
        	MTL=requests.get(url)
	game_id=MTL.text[MTL.text.find(team)-27:MTL.text.find(team)+200]
	team_abr = game_id[game_id.find("ta")+5:game_id.find("ta")+8]
	if 'final' in game_id:
		game_id =  ""
		print "Game Over!"
	else:
		game_id = game_id[game_id.find("id")+4:game_id.find("id")+14]
		print "Today's game ID is : {GameId}".format(GameId=game_id)
	return (game_id,team_abr)

#MAIN

#init        	
old_score=0
new_score=0

print ("When a goal is scored, please press the GOAL button...")
try:
	#team=raw_input("Enter team you want to setup goal light for (Ex: CANADIENS) \n")
        #team=team.upper()
	team="CANADIENS"
	while (1):
		
		
		check_season() #check if in season
		(game_id,team_abr)=check_if_game(team) #check if game tonight/need to update with today's date
			
		while game_id != "":
#			time.sleep(2)
		
			#Check score online and save score
			new_score=fetch_score(game_id,team_abr)
			    
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
			
			(game_id,team_abr)=check_if_game(team)
			
except KeyboardInterrupt:					
	#Restore GPIO to default state
	GPIO.cleanup()
	print ("'\nGPIO cleaned! Goodbye!")
