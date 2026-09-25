# 🎧 Music Taste Analysis & Audio Exploration

This is a personal data science project exploring my music library, listening behaviour, and sonic preferences using Python, analytics, and machine learning.

Music and hi-fi are central interests of mine, and this project is a way to combine that with data science: treating my music taste as a real dataset to explore, visualise, and model.

The project will evolve from basic exploration into deeper analysis such as clustering, taste evolution, and potential recommendation experiments.

---

## 🚀 Project goals

- Build a structured dataset of my music (tracks, artists, audio features, listening history where available)
- Explore patterns in my listening taste through visualisation and statistics
- Identify hidden clusters and “micro-genres” in my library
- Analyse how my taste changes over time
- Experiment with predictive or recommendation-style models
- Produce a portfolio-quality data case study grounded in a real personal interest

---

## 🧱 Planned structure
music-taste/
- data/ # raw and processed datasets
- notebooks/ # exploration, analysis, visualisation
- src/ # reusable scripts and functions
- gemini.md # AI project instructions
- README.md # project overview
---

## 🛠 Tools & stack (provisional)

- Python
- pandas, numpy
- matplotlib, plotly
- scikit-learn
- Jupyter notebooks
- APIs (e.g. Spotify)
- VS Code + AI-assisted development tools

---

## 📈 Example questions this project will explore

- What hidden structures exist in my music library?
- Are there distinct “sound worlds” in my taste?
- How do tempo, energy, rhythm and timbre relate to what I enjoy?
- How has my listening evolved over time?
- Can audio features predict whether I’ll like a track?

---

## 🧠 Motivation

This project is intentionally personal. The aim is to go beyond generic datasets and instead work with something rich, messy, and meaningful.

The long-term goal is to produce a distinctive analytics portfolio project that reflects both technical skills and personal interests in music, sound systems, and culture.

---

## ⚙️ Setup and Installation

1.  **Clone the repository (if not already done):**
    ```bash
    git clone https://github.com/your-username/music-taste.git
    cd music-taste
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file based on your installed packages.)*

4.  **Set up Spotify API Credentials:**
    -   Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    -   Log in and create a new application.
    -   Note down your `Client ID` and `Client Secret`.
    -   Create a file named `.env` in the root directory of this project (next to `README.md`).
    -   Add the following lines to your `.env` file, replacing the placeholders with your actual credentials:
        ```
        SPOTIFY_CLIENT_ID='your_spotify_client_id'
        SPOTIFY_CLIENT_SECRET='your_spotify_client_secret'
        ```
    -   Ensure `.env` is listed in your `.gitignore` file (which it should be now).

---

## 🚀 Usage

### Data Collection

The `src/data_collection.py` script is designed to fetch music data from APIs like Spotify.

1.  **Ensure your virtual environment is active** and `.env` file is configured.
2.  **Run the data collection script:**
    ```bash
    python src/data_collection.py
    ```
    *(This script currently contains placeholders and will require further implementation to fetch real data.)*

### Exploratory Analysis

-   Navigate to the `notebooks/` directory to find Jupyter notebooks for data exploration and visualization.

---