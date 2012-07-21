import model
from model import Movies, User
import movies
from flask import Flask, url_for, render_template, request, redirect, g, session, flash

app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
	g.db = movies.connect_db("dbh36.mongolab.com", 27367, "movie_user", "password", "movies")
	g.db = g.db['movies']
	model.db = g.db
	movies.db = g.db	

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/average', methods=['POST'])
def avg_rating():
	return render_template('avg.html', avg=avg)

@app.route('/details', methods=["POST"])
def movie_details():
	movie_id = int(request.form["movie_id"])
	average_rating = movies.average_rating(movie_id)
	md = Movies.get(movie_id)
	return render_template("details.html", md=md, avg = average_rating)


if __name__ == '__main__':
	app.run(debug=True)