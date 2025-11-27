import streamlit as st
import pandas as pd
import pickle
import requests

# Set up the page layout
st.title('Movie Recommendation System')

# Load the data using caching to speed up the app
@st.cache_resource
def load_data():
    movies_dict = pickle.load(open('movies_data.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open('similarity.pkl', 'rb'))
    similarity = pd.DataFrame(similarity)
    
    return movies, similarity

movies, similarity = load_data()

# API configuration
API_KEY = "" # Your api key

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, API_KEY)
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        full_path = "https://image.tmdb.org/t/p/w500" + data['poster_path']
        return full_path
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity.iloc[movie_index]
    
    # Get top 5 similar movies
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        title = movies.iloc[i[0]].title
        recommended_movies.append({'title': title, 'id': movie_id})
        
    return recommended_movies

# Dropdown menu for selecting movies
selected_movie = st.selectbox(
    'Which movie do you like best?',
    movies['title'].values
)

# Button to trigger recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    
    # Create 5 columns for the layout
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    
    # Lists to store placeholders for posters
    placeholders = []
    
    # Step 1: Display Names Immediately
    for col, movie in zip(cols, recommendations):
        with col:
            # Create a placeholder for the image first (so it stays on top)
            placeholders.append(st.empty())
            # Display the title below
            st.text(movie['title'])
            
    # Step 2: Fetch and Display Posters
    for i, movie in enumerate(recommendations):
        poster_url = fetch_poster(movie['id'])
        placeholders[i].image(poster_url)

