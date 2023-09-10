from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

# formats to highest res allowed
yd = yt.streams.get_highest_resolution()

# add desired folder below
yd.download('./YTfolder')