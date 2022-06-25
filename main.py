from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/most-rated')
def show_most_rated():
    shows = queries.get_most_rated_shows()
    return render_template('shows.html', shows=shows)

@app.route('/show/<int:id>')
def show(id):
    return render_template('show.html', id=id)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
