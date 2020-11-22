import spotify
import youtube

youtube_playlist_url = input(
    "Please paste Youtube Playlist URL here and press enter...\n"
)
spotify_playlist_name = input(
    "Please key in the name for the new Spotify playlist...\n"
)
spotify_playlist_description = input(
    "Please key in the description for the new Spotify playlist...\n"
)

youtube_playlist = youtube.Youtube(youtube_playlist_url)
youtube_playlist.get_youtube_songs()
artist_and_track_names = youtube_playlist.get_youtube_artist_and_track()

spotify_playlist = spotify.Spotify()
spotify_playlist.create_new_spotify_playlist(
    spotify_playlist_name, spotify_playlist_description
)
spotify_playlist.find_spotify_song_url(artist_and_track_names)
spotify_playlist.add_songs_to_spotify_playlist()
