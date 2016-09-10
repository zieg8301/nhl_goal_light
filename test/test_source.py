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
    teamID = team_list[team_list.find("id") + 6:team_list.find("id") + 8]
    return (teamID, team)


def fetch_score1(teamID):
    ########################source 1###################
    now = datetime.datetime.now()
    # url = 'http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date={:%Y-%m-%d}'.format(
    #    teamID, now)
    url = 'http://statsapi.web.nhl.com/api/v1/schedule?teamId={}&date=2016-02-15'.format(
        teamID)
    try:
        score = requests.get(url)
        score = score.text[
            score.text.find(
                "id\" : {}".format(teamID)) -
            37:score.text.find(
                "id\" : {}".format(teamID)) -
            36]
        score = int(score)
        return score
    except requests.exceptions.RequestException:
        print "Error encountered, returning 0 for score"
        return 0


def fetch_score2(team):
    ########################source 2###################
    now = datetime.datetime.now()
    # url = "http://live.nhle.com/GameData/GCScoreboard/date={:%Y-%m-%d}.jsonp".format(
    #    now)
    url = "http://live.nhle.com/GameData/GCScoreboard/date=2016-02-15.jsonp"
    MTL = requests.get(url)
    game_id = MTL.text[MTL.text.find(team):]
    game_id = game_id[MTL.text.find(team):MTL.text.find("id") + 14]
    game_id = game_id[game_id.find("id") + 4:]

    season_id = game_id[:4] + str(int(game_id[:4]) + 1)
    url = "http://live.nhle.com/GameData/{0!s}/{1!s}/gc/gcbx.jsonp".format(
        season_id, game_id)
    try:
        score = requests.get(url)
        score = score.text[score.text.find("goalSummary"):]
        score = score.cout('t1...STL')
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
    teamID, team = get_team()  # choose and return teamID to setup code
    while (1):
	now = datetime.datetime.now()
        time.sleep(2)
        # Check score online and save score
        new_score1 = fetch_score1(teamID)
        #new_score2 = fetch_score2(team)

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
