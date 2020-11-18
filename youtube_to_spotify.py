# 1. Log into Youtube
# 2. Grab our Liked Videos playlist from Youtube
# 3. Create a new playlist on Spotify
# 4. Search for the songs on Spotify
# 5. Add the songs to the new Spotify playlist

from secrets import spotify_user_id, spotify_user_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Create_Playlist:
    def __init__(self):
        self.user_id = spotify_user_id
        pass
        self.spotify_client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=spotify_user_id,
                client_secret=spotify_user_secret,
                redirect_uri="https://localhost/callback/",
                scope="user-library-read playlist-modify-public playlist-modify-private",
            )
        )

    def get_user_saved_tracks(self):
        results = self.spotify_client.current_user_saved_tracks()
        for idx, item in enumerate(results["items"]):
            track = item["track"]
            print(idx, track["artists"][0]["name"], " – ", track["name"])

    def create_new_spotify_playlist(self):
        self.spotify_client.user_playlist_create(
            "subhaac", "Test Playlist", public=True, collaborative=False, description=""
        )
