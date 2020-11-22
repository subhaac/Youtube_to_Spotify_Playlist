from secrets import spotify_user_id, spotify_user_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=spotify_user_id,
                client_secret=spotify_user_secret,
                redirect_uri="https://localhost/callback/",
                scope="playlist-modify-public playlist-modify-private",
            )
        )
        self.uri_list = []
        self.spotify_playlist_id = None

    def create_new_spotify_playlist(self, playlist_name, playlist_description):
        created_playlist = self.spotify_client.user_playlist_create(
            "subhaac",
            playlist_name,
            public=True,
            collaborative=False,
            description=playlist_description,
        )
        self.spotify_playlist_id = created_playlist["id"]

    def find_spotify_song_url(self, song_dict):
        for song in song_dict:
            results = self.spotify_client.search(
                q=str(song + " " + song_dict[song]), limit=1
            )
            for idx, track in enumerate(results["tracks"]["items"]):
                self.uri_list.append(results["tracks"]["items"][0]["uri"])
        return self.uri_list

    def add_songs_to_spotify_playlist(self):
        self.spotify_client.user_playlist_add_tracks(
            user=self.user_id,
            playlist_id=self.spotify_playlist_id,
            tracks=self.uri_list,
        )
