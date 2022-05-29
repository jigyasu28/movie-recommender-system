
# JigyasuFlix
## _The Movie Recommender_



JigyasuFlix is an easy-to-use movie recommender web application. All you need to do is search for a movie and it will show you a similar movie by using a variety of machine learning algorithms.

Currently deployed at [https://nimble-cactus-180569.netlify.app/](https://nimble-cactus-180569.netlify.app/).


## How it looks?

### Homepage
![](screenshots/1.png)
### Search
![](screenshots/2.png)
### Movie Details and Recommendations
![](screenshots/3.jpg)


## How the recommendation engine works?
### [DATASET LINK](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
Content-based filtering was used to recommend movies. Content-based filtering works on the principle that you will also like this other item if you like a particular item. 
* A cluster of words was formed using the overview, keyword, cast, and crew column of the dataset. Then stemming of words was done on the cluster using porterstemmer from python nltk library to get the root form of each word of the cluster. For example words like “retrieval”, “retrieved”, and “retrieves” reduce to their root form “retrieve”. Stop words of English like “is”, “of”, ”and” etc have also been removed for better results.
* The top 5000 most frequently occurred words from the cluster of words from all movies were extracted. They were then used for the construction of a 5000-dimensional vector of each movie. Each word was treated as a dimension and the frequency of that word in the movie became the length of the dimension. 
* Now, to find similar movies for a given movie, cosine distance was calculated between the vector of a particular movie and all other movie vectors. The closest vectors are the most similar movies for that particular movie. The movie recommender then picks the top 30 movies with the least cosine distances.

## How to install?

### Prerequisites: 
* [Python3 and above](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5?hl=en-in&gl=IN)
* [NodeJs18 and above](https://nodejs.org/en/download/)
* [Git](https://git-scm.com/download/win)
* Windows 10 and above.

Clone the repository:
 git clone https://github.com/jigyasu28/movie-recommender-system.git
### For running the backend server:
#### Method 1:
Open backend.bat file.
#### Method 2:
* Go to api folder:
 ``` cd api ```
* Install the api dependencies using command: 
``` pip install -r requirements.txt ```
* Run the setup.py file: 
``` python setup.py ```
* Run the backend server: 
``` python app.py ```
#### Backend will be hosted on http://127.0.0.1:5000/
### For running the frontend:
#### Method 1:
Open frontend.bat file.
#### Method 2:
* Go to client folder:
 ``` cd client ```
* Run commands:<br/>
   1. ``` npm install ```
   2. ``` npm start ```
#### Frontend will be hosted on http://127.0.0.1:3000/
## Technologies Used
* Backend - Python (Flask, Pandas, Pickle, Numpy, Flask-CORS).
* Frontend - ReactJs, Material UI.

## Video Demo
- [https://youtu.be/IjEoe8k_qrE](https://youtu.be/IjEoe8k_qrE)

## Authors

- [@JigyasuJain](https://github.com/jigyasu28)


## Feedback

If you have any feedback, please reach out to us at jigyasujain81@gmail.com
