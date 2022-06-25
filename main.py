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
@app.route('/shows/most-rated/<int:page_number>')
def show_most_rated(page_number=0):
    record_per_page = 15
    shows = queries.get_most_rated_shows(page_number*record_per_page, record_per_page)
    page_count = queries.get_shows_page_count()[0]
    return render_template('shows.html', shows=shows, page_count=page_count["page_count"], page_number=page_number)


@app.route('/show/<int:id>')
def show(id):
    return render_template('show.html', id=id)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
