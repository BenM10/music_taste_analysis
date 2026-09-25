# src/data_collection.py

import os
import argparse
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Load environment variables from a .env file for security
load_dotenv()

# --- Configuration ---
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
# You MUST add this redirect URI to your Spotify app settings on the developer dashboard
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback" 
SCOPE = "user-library-read"

def get_spotify_client():
    """
    Initializes and returns a Spotipy client using user authorization.
    Handles the OAuth 2.0 flow for the user.
    """
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
        raise ValueError(
            "Spotify API credentials not found. Please set SPOTIFY_CLIENT_ID and "
            "SPOTIFY_CLIENT_SECRET in a .env file."
        )

    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SCOPE,
        cache_path=".spotipyoauthcache" # Caches the token to avoid re-authenticating every time
    )
    
    sp = spotipy.Spotify(auth_manager=auth_manager)
    print("Spotify client authenticated.")
    return sp

def fetch_saved_tracks(sp):
    """
    Fetches all of the current user's saved tracks from their library.
    Handles pagination to retrieve all tracks.
    """
    print("Fetching saved tracks...")
  all_tracks = []
    
    # Get total number of saved tracks for progress indication
    try:
        total = sp.current_user_saved_tracks(limit=1)['total']
        print(f"Found {total} saved tracks in your library.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error fetching total tracks: {e}")
        return []

    # The API returns max 50 tracks per request
    limit = 50
    offset = 0
    
    while offset < total:
        try:
            results = sp.current_user_saved_tracks(limit=limit, offset=offset)
            if not results['items']:
                break # No more items to fetch
                
            all_tracks.extend(results['items'])
            offset += len(results['items'])
            print(f"Fetched {offset}/{total} tracks...")

        except spotipy.exceptions.SpotifyException as e:
            print(f"Error fetching tracks at offset {offset}: {e}")
            print("This could be a temporary API issue. Please try again later.")
            break # Stop fetching on error
            
    print(f"\nSuccessfully fetched {len(all_tracks)} track items.")
    return all_tracks

def process_tracks_to_dataframe(tracks, sp=None, with_audio_features=False):
    """
    Processes a list of track items into a clean pandas DataFrame.
    Optionally includes audio features for each track.
    """
    if not tracks:
        print("No tracks to process.")
        return pd.DataFrame()

    print("Processing track data...")
    track_data = []
    track_ids_for_features = []

    for item in tracks:
        track = item.get('track')
        if not track or not track.get('id'):
            continue # Skip if track or track ID is missing

        artists = [artist['name'] for artist in track.get('artists', [])]
        
        track_info = {
            'track_id': track['id'],
            'track_name': track['name'],
            'artist_names': ", ".join(artists),
            'album_name': track.get('album', {}).get('name'),
            'release_date': track.get('album', {}).get('release_date'),
            'popularity': track.get('popularity'),
            'duration_ms': track.get('duration_ms'),
            'explicit': track.get('explicit'),
            'added_at': item.get('added_at')
        }
        track_data.append(track_info)
        
        if with_audio_features:
            track_ids_for_features.append(track['id'])

    df = pd.DataFrame(track_data)
    
    if with_audio_features and track_ids_for_features:
        print("Fetching audio features...")
        df_features = fetch_audio_features(sp, track_ids_for_features)
        if not df_features.empty:
            df = df.merge(df_features, on='track_id', how='left')

    return df

def fetch_audio_features(sp, track_ids):
    """
    Fetches audio features for a list of track IDs in batches.
    Returns a pandas DataFrame of the features.
    """
    if not sp:
        print("Cannot fetch audio features without a Spotify client.")
        return pd.DataFrame()
        
    all_features = []
    batch_size = 100 # Spotify API limit
    
    for i in range(0, len(track_ids), batch_size):
        batch = track_ids[i:i + batch_size]
        try:
            features = sp.audio_features(batch)
            # Filter out None results for invalid track IDs
            all_features.extend([f for f in features if f])
        except spotipy.exceptions.SpotifyException as e:
            print(f"Could not fetch audio features for batch starting at index {i}: {e}")

    df_features = pd.DataFrame(all_features)
    # The audio features response includes an 'id' which is the track_id
    if 'id' in df_features.columns:
        df_features.rename(columns={'id': 'track_id'}, inplace=True)
        
    # Drop columns that are not useful for analysis
    cols_to_drop = ['type', 'uri', 'track_href', 'analysis_url']
    df_features.drop(columns=[col for col in cols_to_drop if col in df_features.columns], inplace=True)

    print("Audio feature fetching complete.")
    return df_features

def main():
    """Main function to run the data collection process."""
    parser = argparse.ArgumentParser(description="Fetch your saved Spotify tracks.")
    parser.add_argument(
        '--with-audio-features',
        action='store_true',
        help="Include audio features for each track (takes longer)."
    )
    args = parser.parse_args()

    try:
        sp = get_spotify_client()
        saved_tracks_items = fetch_saved_tracks(sp)
        
        df = process_tracks_to_dataframe(
            saved_tracks_items, 
            sp=sp, 
            with_audio_features=args.with_audio_features
        )
        
        if not df.empty:
            # Ensure data directory exists
            if not os.path.exists('data'):
                os.makedirs('data')
                
            output_path = 'data/saved_tracks.csv'
            df.to_csv(output_path, index=False)
            print(f"\nSuccessfully saved {len(df)} tracks to {output_path}")

    except ValueError as e:
        print(f"\nConfiguration Error: {e}")
        print("Please ensure your .env file is set up correctly.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("This could be due to a network issue or an invalid setting in your Spotify developer app.")

if __name__ == "__main__":
    main()