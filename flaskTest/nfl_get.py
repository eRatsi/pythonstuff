from flask import Flask, render_template, redirect, abort, url_for
import nflgame
import json

app = Flask(__name__)

@app.route('/')
def index():
	return redirect("http://127.0.0.1:5000/receivers/2013")

@app.route('/receivers/<year>')
def getReceivers(year=None):
	games = nflgame.games(int(year))
	players = nflgame.combine(games)
	myQuery = {}
	for p in players.receiving().sort("receiving_yds").limit(10):
		myQuery[str(p)] = p.receiving_yds
	return render_template('index.html', year=year, myQuery=myQuery, player="receivers")

@app.route('/rushers/<year>')
def getRushers(year=None):
	games = nflgame.games(int(year))
	players = nflgame.combine(games)
	myQuery = {}
	for p in players.rushing().sort("rushing_yds").limit(10):
		myQuery[str(p)] = p.rushing_yds
	return render_template('index.html', year=year, myQuery=myQuery, player="rushers")

if __name__=="__main__":
	app.run()