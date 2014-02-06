from flask import Flask, render_template, redirect, abort, url_for
import nflgame
import json

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<year>')
def hello(year=None):
	games = nflgame.games(int(year))
	players = nflgame.combine(games)
	myQuery = {}
	for p in players.receiving().sort("receiving_yds").limit(10):
		myQuery[str(p)] = p.receiving_yds
	return render_template('index.html', year=year, myQuery=myQuery)


if __name__=="__main__":
	app.run()