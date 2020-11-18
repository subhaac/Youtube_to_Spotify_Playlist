from secrets import spotify_user_id, spotify_user_secret
import youtube_to_spotify as YTS

new_playlist = YTS.Create_Playlist()
new_playlist.get_user_saved_tracks()
new_playlist.create_new_spotify_playlist()
