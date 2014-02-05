import nflgame
import json

def getRushers(players):
	myQuery = []
	for p in players.rushing().sort("rushing_yds").limit(10):
		myQuery.append({"name": p, "rushing yards" : p.rushing_yds})
	return json.dumps(myQuery)

def getPlayers(year):
	games = nflgame.games(year)
	players = nflgame.combine(games)
	return players

def getReceivers(players):
	myQuery = []
	for p in players.receiving().sort("receiving_yds").limit(10):
		myQuery.append({"name" : p, "receiving yards" : p.receiving_yds})
	return json.dumps(myQuery)