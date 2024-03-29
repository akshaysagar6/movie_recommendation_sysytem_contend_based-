import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]#to get the index of movies
    movie_sim = pickle.load(open('sim.pkl', 'rb'))
    distance=movie_sim[movie_index].argsort()[:-11:-1]#find the index of top similar movies from sovie_sim matrix, #gives top 5 movie index

    movie_recom=movies.loc[distance]
    movies_recommend=movie_recom['title']
    return movies_recommend

movie_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movie_list)

st.title('Movie Recommender System')


selected_movie=st.selectbox("How Would you Like To Connect", movies['title'].values)

if st.button("Recommend"):
    names=recommend(selected_movie)
    for i in names:
        st.write(i)

