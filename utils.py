import spotipy
import pandas as pd

def get_songs_in_year(df, year):
    mask = df.year.apply(lambda x: x == int(year))
    return df[mask]

def get_artist_albums(artist_id, sp=None):
    if not sp:
        sp = spotipy.Spotify()
    return sp.artist_albums(artist_id)

def get_album_tracks(album_id, sp=None):
    if not sp:
        sp = spotipy.Spotify()
    return sp.album_tracks(album_id)

def get_all_artist_ids():
    sp = spotipy.Spotify()
    df = pd.read_csv("./data/top_1000_artists.csv")
    artists = df['Artist Name']
    artist_ids = [""] * len(artists)
    for i, artist in enumerate(artists):
        results = sp.search(q='artist:' + artist, type='artist')
        artist_id = results['artists']['items'][0]['id']
        artist_ids[i] = artist_id
    # fix this
    artists_df = pd.concat([artists, pd.Series(artist_ids).values], axis=1)
    artists_df.to_csv("./data/artists_with_ids.csv")
    print("Finished getting ids for all artists")

def get_all_artist_albums():
    sp = spotipy.Spotify()
    df = pd.read_csv("./data/artists_with_ids.csv")
    artist_ids = df['artist_ids']
    album_ids = []
    for i, artist_id in enumerate(artist_ids):
        albums = sp.artist_albums(artist_id)
        album_ids.append((artist_id, albums))
    return album_ids
