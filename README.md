# Netflix-Analytics-Popularity-Prediction-and-Recommendation-System
Netflix Analytics, Popularity Prediction & Recommendation System

An AI-powered Netflix analytics platform that combines data analytics, machine learning, NLP, recommendation systems, and interactive visualization to create a personalized streaming experience. The platform analyzes Netflix datasets, predicts content popularity, recommends similar titles, and provides real-time content insights through an interactive Netflix-inspired interface.

Built with a multi-page Streamlit architecture, the project delivers a modern UI with trending sections, content cards, analytics dashboards, and real-time movie poster integration.

Installation & Setup

Clone repository:

git clone <repository-url>

Move to project directory:

cd Netflix-Analytics

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py

Features
Interactive Netflix Analytics Dashboard
Top 10 Trending Movies
Top 10 Trending TV Shows
Content growth analysis over years
Rating distribution visualizations
Genre-wise insights
Movie vs TV Show comparisons
Catalog statistics
Interactive charts and dashboards
Popularity Prediction System

Predicts content popularity on a 0–10 scale using machine learning.

**Features used:

Content Type
Release Year
Rating
Country
Genre
Duration

Model:

Random Forest Regressor

Output:

Predicted popularity score
Movie details
Poster visualization
Content metadata
Intelligent Recommendation Engine

Provides personalized recommendations using Natural Language Processing techniques.

Recommendation logic considers:

Genre similarity
Description similarity
Cast similarity
Director similarity
Franchise detection

Example:

Final Destination
↓
Final Destination 2
↓
Final Destination 3
↓
Related Horror Titles
Personalized Content Filtering

Users can discover content through filters:

Genre
Rating
Release Year
Content Type
Real-Time Poster Integration

Integrated with TMDB API:

Automatic movie poster retrieval
Retry handling
Request caching
Timeout handling
Session reuse
Fallback support
Project Architecture
Dataset
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Popularity Prediction Model
   ↓
Recommendation Engine
   ↓
TMDB API Integration
   ↓
Streamlit Frontend
Machine Learning Pipeline
Data Preprocessing

Performed:

Missing value handling
Data cleaning
Date conversion
Label encoding
Numerical transformations
Text preprocessing
Feature Engineering

Created additional features:

Recency Score

Measures content freshness

Genre Score

Measures genre popularity trends

Duration Score

Extracts numerical duration values

Content-Type Score

Movie vs TV weighting

Recommendation Pipeline

Combined text fields:

Genres
Description
Cast
Director

Applied:

TF-IDF Vectorization

Generated:

Cosine Similarity Matrix

Used for intelligent recommendations.

Tech Stack
Frontend
Streamlit
HTML
CSS

Purpose:

Multi-page application
Netflix-inspired UI
Interactive dashboards
Backend
Python

Purpose:

Business logic
ML pipeline
Data processing
API handling
Data Processing
Pandas
NumPy

Used for:

Data cleaning
Transformations
Aggregation
Feature engineering
Data Visualization
Matplotlib
Seaborn

Used for:

Trend analysis
Comparative charts
Rating distribution
Analytics dashboards
Machine Learning
Scikit-Learn
Random Forest Regressor
Label Encoder
TF-IDF Vectorizer
Cosine Similarity

Used for:

Popularity prediction
Recommendation engine
NLP pipeline
API Integration
TMDB API
Requests

Optimizations:

Session reuse
Retry mechanisms
Request caching
Timeout handling
Deployment
Streamlit Cloud
Docker
GitHub
