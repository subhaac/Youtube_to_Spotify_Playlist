import pytube

url = input("Please enter your playlist URL")
playlist = pytube.Playlist(url)

print("There are " + str(len(playlist.video_urls)) + "videos") 