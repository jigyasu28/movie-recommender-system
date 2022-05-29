# from urllib import response
import flask
from flask import Flask,abort
import pickle
import pandas as pd
# from pyparsing import Word
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
similarity = pickle.load(open('similarity.pkl','rb'))

print(list_of_movies[list_of_movies.movie_id == 49026], "line 26")
# search of movie by genre
def findByGenre(genres, required_genre):
    if len(genres) and required_genre == genres[0]:
        return True
    else:
        return False


def findMovieByGenre(genre):
    arr = []
    for i in range(len(list_of_movies)):
        check = findByGenre(list_of_movies.iat[i, 3], genre)
        arr.append(check)
    print(list_of_movies.head())
    
    return list_of_movies[arr]

# [(1, 'n1'), (2, 'n2')]
# [('n1')]
# (1, 'n1')[name] = 'n1'

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
    print('genre=' , value)
    response = findMovieByGenre(value)
    # print("type of response",type(response))
    #print(response)
    # shuffled = response.sample(frac=1).reset_index
    # print("shuffled",type(shuffled))
    return response.head(20).to_json(orient = "records")

def getId(similar_movies):
    arr=[]
    for i in range(len(similar_movies)):
        arr.append[similar_movies[i][0]]
    return arr


def recommended(movie):
    index = list_of_movies[list_of_movies['title'] == movie].index[0]
    distances = similarity[index]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:33]
    id = list(map(lambda x: x[0],similar_movies))
    movieIds = list_of_movies.iloc[id]
    # print(movieIds)
    return movieIds
# recommended("Avatar")

@app.route('/getRecommendation/', methods=["POST", "OPTIONS"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def movies():
    req = flask.request.json
    value = req["id"]
    
    #print(response)
    movie = list_of_movies[list_of_movies.movie_id == value].iloc[0]["title"]
    response = recommended(movie)
    return response.to_json(orient="records")

if __name__ == '__main__':
	app.run(debug=True)