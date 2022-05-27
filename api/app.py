import flask
from flask import Flask,abort
import pickle
import pandas as pd
from pyparsing import Word
import requests
import json, sys
from flask_cors import CORS, cross_origin
import numpy as np



app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# loading of files
list_of_movies_dict = pickle.load(open('movie_dict2.pkl','rb'))
list_of_movies = pd.DataFrame(list_of_movies_dict)
list_of_movies["index"] = list_of_movies.index
# print(list_of_movies.head().title)
print(list_of_movies.head())
similarity = pickle.load(open('similarity.pkl','rb'))



# search of Word
def check_of_genre(genre, string):
    return genre in string



def category(name):
    arr = []
    # for i in range(len(list_of_movies)):
    #     check = check_of_genre(name, list_of_movies.iat[i,2])
    #     if check:
    #         arr.append(list_of_movies.iat[i,2])
    searchByName = np.vectorize(lambda x: name.lower() in x.lower())
    res = searchByName(list_of_movies.title)
    print(res)
    return list_of_movies[res]

category('a')

# print(list_of_movies)


# print(list_of_movies['title'][0])
# print(type(list_of_movies))
@app.route('/search/', methods=["POST", "OPTIONS"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def extra():
    req = flask.request.json
    value = req["value"]
    response = category(value)
    return response.head(5).to_json(orient = "records")


@app.route('/getGenreMovie/', methods=["POST", "OPTIONS"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def getGenre():
    req = flask.request.json
    value = req["genre"]
    response = list_of_movies
    return response.head(10).to_json(orient = "records")

if __name__ == '__main__':
	app.run(debug=True)