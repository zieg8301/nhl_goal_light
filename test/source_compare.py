#!/usr/bin/python

import datetime
import time
import os
import requests

#import requests_cache
# requests_cache.install_cache()
# requests_cache.clear()

f1 = open('./testfile.log', 'a')


def get_team():
	""" Function to get team of user and return NHL team ID. Default team is CANADIENS. """
    team = raw_input(
        "Enter team you want to setup goal light for (Default: CANADIENS) \n")
    if team is "":
        team = "Canadiens"
    team = team.title()
    url = 'http://statsapi.web.nhl.com/api/v1/teams'
    team_list = requests.get(url)
    team_list = team_list.text[
        team_list.text.find(team) -
        50:team_list.text.find(team)]
    team_id = team_list[team_list.find("id") + 6:team_list.find("id") + 8]
    return (team_id, team)


def fetch_score1(team_id):
	""" Function to get the score of the game depending on the chosen team. Inputs the team ID and returns the score found on web. """
    ########################source 1###################
    now = datetime.datetime.now()
    url = 'http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date={:%Y-%m-%d}'.format(
       team_id, now)

    try:
        score = requests.get(url)
        score = score.text[
            score.text.find(
                "id\" : {}".format(team_id)) -
            37:score.text.find(
                "id\" : {}".format(team_id)) -
            36]
        score = int(score)
        return score
    except requests.exceptions.RequestException:
        print "Error encountered, returning 0 for score"
        return 0


def fetch_score2(team,team_id):
	""" Function to get the score of the game depending on the chosen team. Inputs the team ID and returns the score found on web. """
    ########################source 2###################
    now = datetime.datetime.now()
    # url = "http://live.nhle.com/GameData/GCScoreboard/date={:%Y-%m-%d}.jsonp".format(
    #    now)
    url = 'http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date={:%Y-%m-%d}'.format(
       team_id, now)
    MTL = requests.get(url)
    game_id = MTL.text[MTL.text.find("gamePk") + 10:]
    if (now.month >= 9) :
    	season_id = str(now.year) + str(now.year + 1)
    else :
    	season_id = str(now.year - 1) + str(now.year)
    url = "http://live.nhle.com/GameData/{0}/{1}/gc/gcbx.jsonp".format(
        season_id, game_id)
    try:
        score = requests.get(url)
        score = score.text[score.text.find("goalSummary"):]
        score = score.cout('t1...MTL')
        return score
    except requests.exceptions.RequestException:
        print "Error encountered, returning 0 for score"
        return 0

#if __name__ == "__main__":

old_score1 = 0
new_score1 = 0

old_score2 = 0
new_score2 = 0

print ("When a goal is scored, press the GOAL button...")
try:
    team_id, team = get_team()  # choose and return teamID to setup code
    while (1):
	now = datetime.datetime.now()
        time.sleep(2)
        # Check score online and save score
        new_score1 = fetch_score1(team_id)
        new_score2 = fetch_score2(team,team_id)

        # If score change...
        if new_score1 > old_score1:
            # save new score
            old_score1 = new_score1
	    text = ("GOAL source 1! Time : " + str(now.hour)+":" + str(now.minute)+":" + str(now.second)+"\n")
            f1.write(text)
	    print ("source1 goal")

        elif new_score2 > old_score2:
            # save new score
            old_score2 = new_score2
            text = ("GOAL source 2! Time : " + str(now.hour)+":" + str(now.minute)+":" + str(now.second)+"\n")
            f1.write(text)
            print("source2 goal")

except KeyboardInterrupt:
    # requests_cache.clear()
    # print "\nCache cleaned!"
    print "Thank you! Goodbye!"
