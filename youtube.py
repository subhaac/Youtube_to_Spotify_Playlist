import pytube
import youtube_dl


class Youtube:
    def __init__(self, url):
        self.youtube_playlist = pytube.Playlist(url)
        self.list_of_songs = []
        self.song_dict = {}
        pass

    def get_youtube_songs(self):
        for song in self.youtube_playlist.video_urls:
            try:
                self.list_of_songs.append(song)
            except Exception:
                pass
        return self.list_of_songs

    def get_youtube_artist_and_track(self):
        for songs in self.list_of_songs:
            download = False
            ydl_opts = {
                "outtmpl": "fileName",
                "writethumbnail": True,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ie_result = ydl.extract_info(songs, download)

            try:
                self.song_dict[ie_result["track"]] = ie_result["artist"]
            except Exception as e:
                print("Exception: ", e)
                continue
        return self.song_dict
