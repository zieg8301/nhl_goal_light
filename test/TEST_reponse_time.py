#!/usr/bin/python

import datetime
import time, os, random
import requests
#import requests_cache

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
	teamID=team_list[team_list.find("id")+6:team_list.find("id")+8]
	return teamID

def fetch_score(teamID):
	now=datetime.datetime.now()
        url='http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date={:%Y-%m-%d}'.format(teamID,now)
	score=requests.get(url)
	score=score.text[score.text.find("id\" : {}".format(teamID))-37:score.text.find("id\" : {}".format(teamID))-36]
	score=int(score)
	print (score,now.hour, now.minute, now.second)
	return score

def check_season():
	now = datetime.datetime.now()
	if now.month in (7, 8, 9):
            	return False
	else:
		return True

def check_if_game(teamID):
	#embed()
	now=datetime.datetime.now()
        url='http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date={:%Y-%m-%d}'.format(teamID,now)
        gameday_url=requests.get(url)
	if "gamePk" in gameday_url.text:
		return True
	else:
		return False
def sleep(sleep_period):
	now=datetime.datetime.now()
   	if "day" in sleep_period:
     		delta=datetime.timedelta(days=1)
	elif "season" in sleep_period:
		if now.month is 8:
			delta=datetime.timedelta(days=31)
		else:
			delta=timedelta(days=30)
    	next_day=datetime.datetime.today()+delta
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
	teamID=get_team() #choose and return teamID to setup code
	while (1):
		season=check_season() #check if in season
		gameday=check_if_game(teamID) #check if game	
		
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
					print ("GOAL! Time : ",now.hour, now.minute, now.second)
			
			else:
				print "No Game Today!"
				sleep("day")
		else:
			print "OFF SEASON!"
			sleep("season")
						
except KeyboardInterrupt:					
	#requests_cache.clear()
	#print "\nCache cleaned!"
	print "Thank you! Goodbye!"
	
