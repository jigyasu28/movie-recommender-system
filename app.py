import streamlit as st
import pickle
import pandas as pd
import requests

st.title('My movie reccomendor')


#LOADING REQUIRED PKL FILES
list_of_movies_dict = pickle.load(open('movie_dict.pkl','rb'))
list_of_movies = pd.DataFrame(list_of_movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

#fetching poster from api using movie id
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=03f4b7c839caf675aaecbbf85e86257a&language=en-US'.format(movie_id))
    poster_data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + poster_data['poster_path']

#SEARCH FUNCTION 
def search_result(name):
    index = list_of_movies[list_of_movies['title'] == name].index[0]
    distances = similarity[index]
    similar_movies = sorted(list(enumerate(distances)),reverse = True,key = lambda x : x[1])[1:6]
    similar_movies_poster = []
    result = []
    for i in similar_movies:
        result.append(list_of_movies.iloc[i[0]].title)
        #fetching poster through api
        similar_movies_poster.append(fetch_poster(list_of_movies.iloc[i[0]].movie_id))
    return result,similar_movies_poster



#SEARCH BAR AND BUTTON
option_selected = st.selectbox(
     'Search your favorite movie', list_of_movies['title'].values)
st.write('You selected:', option_selected)

if st.button('Search'):
    name,posters = search_result(option_selected)
    col = st.columns(5)
    for i in range(0,5):
        with col[i]:
            st.text(name[i])
            st.image(posters[i])
