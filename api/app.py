# Using content based filtering to recommend movies. 
import flask
from flask import Flask,abort
import pickle
import pandas as pd
import requests
import json, sys
from flask_cors import CORS, cross_origin
import numpy as np


# Calling Flask and CORS.
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# loading of files.
list_of_movies_dict = pickle.load(open('movie_dict2.pkl','rb'))
list_of_movies = pd.DataFrame(list_of_movies_dict)
list_of_movies["index"] = list_of_movies.index
similarity = pickle.load(open('similarity.pkl','rb'))

print(list_of_movies[list_of_movies.movie_id == 49026], "line 26")


# Searching for a particular genre the movie genre list.
def findByGenre(genres, required_genre):
    if len(genres) and required_genre == genres[0]:
        return True
    else:
        return False

# Searching movie using genres.
def findMovieByGenre(genre):
    arr = []
    for i in range(len(list_of_movies)):
        check = findByGenre(list_of_movies.iat[i, 3], genre)
        arr.append(check)
    print(list_of_movies.head())
    
    return list_of_movies[arr]

# Search results in search bar.
def category(name):
    arr = []
    searchByName = np.vectorize(lambda x: name.lower() in x.lower())
    res = searchByName(list_of_movies.title)
    print(res)
    return list_of_movies[res]

category('a')

# Sending search results using post method.
@app.route('/search/', methods=["POST", "OPTIONS"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def extra():
    req = flask.request.json
    value = req["value"]
    response = category(value)
    return response.head(5).to_json(orient = "records")

# Sending results based on genres.
@app.route('/getGenreMovie/', methods=["POST", "OPTIONS"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def getGenre():
    req = flask.request.json
    value = req["genre"]
    print('genre=' , value)
    response = findMovieByGenre(value)
    return response.head(20).to_json(orient = "records")

# Getting the id of similar movies.
def getId(similar_movies):
    arr=[]
    for i in range(len(similar_movies)):
        arr.append[similar_movies[i][0]]
    return arr

# Collecting top 30 similar movieIds.
def recommended(movie):
    index = list_of_movies[list_of_movies['title'] == movie].index[0]
    distances = similarity[index]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:33]
    id = list(map(lambda x: x[0],similar_movies))
    movieIds = list_of_movies.iloc[id]
    return movieIds


# Sending recommendations based on user search through post method.
@app.route('/getRecommendation/', methods=["POST", "OPTIONS"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def movies():
    req = flask.request.json
    value = req["id"]
    movie = list_of_movies[list_of_movies.movie_id == value].iloc[0]["title"]
    response = recommended(movie)
    return response.to_json(orient="records")

if __name__ == '__main__':
	app.run(debug=True)
