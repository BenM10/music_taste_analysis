# Gemini Project Instructions — Music Taste Analysis

This project explores my personal music library and listening taste using data science and analytics.

The goals of this project are to:
- Build a clean dataset of my music (tracks, artists, audio features, listening history where available)
- Explore and visualise patterns in my taste
- Discover hidden clusters, trends, and structures in what I listen to
- Gradually build toward more advanced analysis (clustering, embeddings, recommendation ideas)

## Project style & expectations

- Prioritise clear, readable, well-structured code over clever or overly abstract solutions
- Prefer pandas, numpy, matplotlib/plotly, scikit-learn, and Jupyter notebooks for exploration
- Explain what code is doing when introducing new concepts
- Break large tasks into small, testable steps
- Avoid overengineering — this is an exploratory analytics project

## Folder structure conventions

When creating files, prefer:

- `data/` → raw and processed datasets (CSV, JSON, etc.)
- `notebooks/` → exploration, visualisations, experiments
- `src/` → reusable Python scripts and functions
- `README.md` → human-readable project overview

Do not place large datasets under version control by default.

## How to work in this project

- Always check what files already exist before creating new ones
- Ask before restructuring folders
- Prefer incremental builds over big monolithic scripts
- When pulling data from APIs, separate:
  - data collection
  - data cleaning
  - analysis

---

## ⚙️ Setup and Installation

1.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Spotify API Credentials:**
    -   Create a file named `.env` in the root directory of this project.
    -   Add your `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` to this file:
        ```
        SPOTIFY_CLIENT_ID='your_spotify_client_id'
        SPOTIFY_CLIENT_SECRET='your_spotify_client_secret'
        ```
    -   Ensure `.env` is listed in your `.gitignore` file.

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

---

## Long-term direction

This project may later include:
- clustering of tracks into emergent genres
- taste evolution over time
- rhythm and audio-feature analysis
- personal recommendation experiments

The aim is to make this both a learning project and a portfolio-quality case study.