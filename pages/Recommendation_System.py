import streamlit as st
import pandas as pd
import requests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

st.title("Movie Recommendation System")

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("NetFlix.csv")

df.fillna("", inplace=True)

# -----------------------------
# Poster Fetch Function
# -----------------------------

def fetch_poster(movie_title):

    api_key = "869041fc5ee78743f0ae07adc0c69a0d"

    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"

    response = requests.get(url)

    data = response.json()

    if len(data["results"]) > 0:

        poster_path = data["results"][0]["poster_path"]

        if poster_path:
            poster_url = "https://image.tmdb.org/t/p/w500" + poster_path
            return poster_url

    return None


# -----------------------------
# Combine Features
# -----------------------------

df["combined_features"] = (
    df["genres"] + " " +
    df["description"] + " " +
    df["cast"] + " " +
    df["director"]
)

# -----------------------------
# TF-IDF Vectorization
# -----------------------------

vectorizer = TfidfVectorizer(stop_words="english")

feature_matrix = vectorizer.fit_transform(df["combined_features"])

# -----------------------------
# Cosine Similarity
# -----------------------------

similarity_matrix = cosine_similarity(feature_matrix)

# -----------------------------
# Movie Selection UI
# -----------------------------

movie_list = df["title"].values

selected_movie = st.selectbox(
    "Select a Movie",
    movie_list
)

# -----------------------------
# Recommendation Logic
# -----------------------------

# -----------------------------
# Recommendation Logic
# -----------------------------

if st.button("Recommend Movies"):

    movie_index = df[df.title == selected_movie].index[0]

    # detect franchise name
    base_name = selected_movie.split(":")[0].split(" - ")[0]

    # find franchise movies
    franchise_movies = df[df["title"].str.contains(base_name, case=False, na=False)]

    recommendations = []

    # add franchise movies first
    for _, row in franchise_movies.iterrows():

        if row["title"] != selected_movie:
            recommendations.append(row["title"])

    # similarity recommendations
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    sorted_movies = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    for movie_idx, score in sorted_movies:

        movie_title = df.iloc[movie_idx]["title"]

        if movie_title not in recommendations and movie_title != selected_movie:

            recommendations.append(movie_title)

        if len(recommendations) >= 5:
            break

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i, movie_title in enumerate(recommendations[:5]):

        poster = fetch_poster(movie_title)

        with cols[i]:

            if poster:
                st.image(poster)

            st.write(movie_title)