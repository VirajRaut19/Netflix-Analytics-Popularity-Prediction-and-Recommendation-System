import streamlit as st
import pandas as pd
import requests
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="Popularity Predictor",
    layout="wide"
)

st.title("Movie Popularity Predictor")

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("NetFlix.csv")

df.fillna("Unknown", inplace=True)

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
            return "https://image.tmdb.org/t/p/w500" + poster_path

    return None


# -----------------------------
# Realistic Popularity Calculation
# -----------------------------

current_year = df['release_year'].max()

df['recency_score'] = 1 - (
    (current_year - df['release_year']) /
    (current_year - df['release_year'].min())
)

genre_counts = df['genres'].value_counts()

df['genre_score'] = df['genres'].map(genre_counts)
df['genre_score'] = df['genre_score'] / df['genre_score'].max()

df['type_score'] = df['type'].apply(lambda x: 1 if x == "Movie" else 0.8)

df['duration_num'] = df['duration'].astype(str).str.extract('(\d+)').astype(float)

df['duration_score'] = df['duration_num'] / df['duration_num'].max()

df['popularity'] = (
    0.4 * df['recency_score'] +
    0.3 * df['genre_score'] +
    0.2 * df['type_score'] +
    0.1 * df['duration_score']
) * 10


# -----------------------------
# Encode Data
# -----------------------------

le = LabelEncoder()

df['type'] = le.fit_transform(df['type'])
df['rating'] = le.fit_transform(df['rating'])
df['country'] = le.fit_transform(df['country'])
df['genres'] = le.fit_transform(df['genres'])


# -----------------------------
# Train Model
# -----------------------------

X = df[['type','release_year','rating','country','genres']]
y = df['popularity']

model = RandomForestRegressor()
model.fit(X, y)


# -----------------------------
# Prediction UI
# -----------------------------

movie_name = st.selectbox(
    "Select Movie",
    sorted(df['title'].unique())
)

movie = df[df['title'] == movie_name]

if st.button("Predict Popularity Score"):

    features = movie[['type','release_year','rating','country','genres']]

    prediction = model.predict(features)

    poster = fetch_poster(movie_name)

    col1, col2 = st.columns([1,2])

    with col1:

        if poster:
            st.image(poster, width=300)
        else:
            st.write("Poster not available")

    with col2:

        st.subheader(movie_name)

        st.metric(
            "Predicted Popularity",
            round(prediction[0], 2)
        )

        st.metric(
            "Release Year",
            int(movie['release_year'].values[0])
        )

        st.metric(
            "Rating",
            movie['rating'].values[0]
        )