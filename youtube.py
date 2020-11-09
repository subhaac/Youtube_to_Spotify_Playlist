import pytube

class Youtube_Playlist():
    list_of_songs = []
    def __init__(self, url):
        self.playlist = pytube.Playlist(url)

    def get_songs(self):
        """Returns a list of URLs of the songs in the playlist

        Returns:
            [list]: [list of URLs of songs]
        """
        for song in self.playlist.video_urls:
            self.list_of_songs.append(song)
        return self.list_of_songs
        
    def __sizeof__(self):
        return "OK"
