from secrets import spotify_user_id, spotify_user_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pytube
import youtube_dl


class Create_Playlist:
    list_of_songs = []

    def __init__(self, url):
        self.user_id = spotify_user_id
        self.youtube_playlist = pytube.Playlist(url)
        self.spotify_client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=spotify_user_id,
                client_secret=spotify_user_secret,
                redirect_uri="https://localhost/callback/",
                scope="user-library-read playlist-modify-public playlist-modify-private",
            )
        )
        self.song_dict = {}

    def get_user_saved_tracks_from_spotify(self):
        results = self.spotify_client.current_user_saved_tracks()
        for idx, item in enumerate(results["items"]):
            track = item["track"]
            print(idx, track["artists"][0]["name"], " – ", track["name"])

    def create_new_spotify_playlist(self):
        self.spotify_client.user_playlist_create(
            "subhaac",
            "Songs from Youtube",
            public=True,
            collaborative=False,
            description="Songs transferred from Youtube playlist",
        )

    def get_youtube_songs(self):
        for song in self.youtube_playlist.video_urls:
            try:
                self.list_of_songs.append(song)
            except Exception:
                pass
        return self.list_of_songs

    def get_youtube_artist_and_track(self):
        for songs in range(0, 4):
            download = False
            ydl_opts = {
                "outtmpl": "fileName",
                "writesubtitles": True,
                "format": "mp4",
                "writethumbnail": True,
                "ignoreerrors": True,
                "skipdownload": True,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ie_result = ydl.extract_info(self.list_of_songs[songs], download)

            try:
                self.song_dict[ie_result["track"]] = ie_result["artist"]
            except Exception as e:
                print("Exception: ", e)
                continue
        return self.song_dict

    def find_spotify_song_url(self):
        for song in self.song_dict:
            results = self.spotify_client.search(
                q=str(song + " " + self.song_dict[song]), limit=1
            )
            # print(results["tracks"]["items"])
            # print()
            for idx, track in enumerate(results["tracks"]["items"]):
                print(idx, track["name"])
                print(results["tracks"]["items"][0]["uri"])
