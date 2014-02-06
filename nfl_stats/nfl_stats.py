import nflgame
import json

def getRushers(players, myQuery):
	myQuery += "\"rushers\": {\n\t\t"
	for p in players.rushing().sort("rushing_yds").limit(10):
		myQuery += "\"name\": \"%s\",\n\t\t" % str(p)
		myQuery += "\"rushing_yds\": \"%s\",\n\t\t" % p.rushing_yds
	myQuery += "}\n}"
	return myQuery

def getPlayers(year):
	games = nflgame.games(year)
	players = nflgame.combine(games)
	return players

def getReceivers(players):
	myQuery = "{\n\t\"receivers\": {\n\t\t"
	for p in players.receiving().sort("receiving_yds").limit(10):
		myQuery += "\"name\": \"%s\",\n\t\t" % str(p)
		myQuery += "\"receiving_yds\": \"%s\",\n\t\t" % p.receiving_yds
	myQuery += "},\n\t"
	return myQuery

def main():
	players = getPlayers(2013)
	finalJSON = getRushers(players, getReceivers(players))
	print finalJSON
	return json.dumps(finalJSON)

if __name__ == '__main__':
	main()