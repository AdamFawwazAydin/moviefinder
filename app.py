from flask import Flask, render_template, request
import requests

app = Flask(__name__)

import os
API_KEY = os.getenv("API_KEY")

# HOME (SEARCH)
@app.route('/', methods=['GET', 'POST'])
def index():
    movies = []
    error = None

    if request.method == 'POST':
        query = request.form['query']

        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={query}"
        response = requests.get(url)
        data = response.json()

        if data.get('Response') == 'True':
            movies = data['Search']
        else:
            error = data.get('Error')

    return render_template('index.html', movies=movies, error=error)


# DETAIL FILM
@app.route('/detail/<imdb_id>')
def detail(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}&plot=full"
    response = requests.get(url)
    movie = response.json()

    return render_template('detail.html', movie=movie)


if __name__ == '__main__':
    app.run(debug=True)
