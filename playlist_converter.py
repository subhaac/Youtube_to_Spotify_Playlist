import youtube_to_spotify as YTS


youtube_playlist_url = input(
    "Please paste Youtube Playlist URL here and press enter...\n"
)
spotify_playlist_name = input(
    "Please key in the name for the new Spotify playlist...\n"
)
spotify_playlist_description = input(
    "Please key in the description for the new Spotify playlist...\n"
)


new_playlist = YTS.Create_Playlist(youtube_playlist_url)

new_playlist.get_youtube_songs()

new_playlist.get_youtube_artist_and_track()

new_playlist.create_new_spotify_playlist(
    spotify_playlist_name, spotify_playlist_description
)

new_playlist.find_spotify_song_url()

new_playlist.add_songs_to_spotify_playlist()