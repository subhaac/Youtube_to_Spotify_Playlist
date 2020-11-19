from secrets import spotify_user_id, spotify_user_secret
import youtube_to_spotify as YTS

new_playlist = YTS.Create_Playlist(
    "https://www.youtube.com/playlist?list=PLDZ4oq5DYxerIotuyCO69JKotjXaAdfvz"
)
# new_playlist.get_user_saved_tracks()
# new_playlist.create_new_spotify_playlist()

new_playlist.get_youtube_songs()

print(new_playlist.get_youtube_artist_and_track())