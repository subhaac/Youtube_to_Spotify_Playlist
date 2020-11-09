import youtube 


converter_direction = input("Youtube > Spotify or Spotify > Youtube? Please answer Y or S\n")
print(converter_direction)

input_url = input("Please input source playlist URL\n")
new_playlist = youtube.Youtube_Playlist(input_url)
print(new_playlist.get_songs())