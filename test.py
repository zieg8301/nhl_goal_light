from datetime import datetime
import time, os, random
import requests
#import RPi.GPIO as GPIO
import subprocess, ctypes


def check_if_game():
	
	now=datetime.now()
        url="http://live.nhle.com/GameData/GCScoreboard/%s.jsonp" % (now.strftime("%Y-%m-%d"))
	#MTL=subprocess.check_output("wget -O- %s" % url, "| grep -o 'MTL'", shell=True)
        MTL=requests.get(url)
	#print MTL.text
	if "MTL" in MTL.text:
		return True
	else:
		return False


def fetch_score():
	#score=subprocess.check_output("wget -O- http://live.nhle.com/GameData/20152016/2015021091/gc/gcbx.jsonp -nv | grep -o 'goalSummary.*' | grep -o 't1...MTL' | wc -l", shell=True)
	score=requests.get("http://live.nhle.com/GameData/20152016/2015021091/gc/gcbx.jsonp")
	score=score.text.cout('t1...MTL')
	return score


if_game=check_if_game()
while (1):
	if_game=check_if_game()
	if if_game:
		score=fetch_score()
		print score
	time.sleep(1)
