import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def loadObject(PATH):
    with open(PATH, "rb") as inp:
        print("similarity matrix found")
        obj = pickle.load(inp)
    return obj

def initializeSimilarity(PATH):
    new_df = loadObject(PATH)
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()
    similarity = cosine_similarity(vectors)
    pickle.dump(similarity, open('similarity.pkl', 'wb'))

    return similarity


def loadSimilarity(PATH):
    print("Loading similarity")
    try:

        similarity = loadObject(PATH)
    except:
        print("similarity matrix not found ! creating now")
        similarity = initializeSimilarity("movie_dict2.pkl")
    
    print("similarity matrix loaded")
    return similarity

similarity = loadSimilarity('similarity.pkl')
