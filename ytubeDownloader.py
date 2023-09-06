from pytube import YouTube
from sys import argv
#argv takes all the things you input into command line in this program

link = argv[1]
#do not use index 0 as 0 is reserved for the program name
yt = YouTube(link)

print("The Title of the video":, yt.title)

print("Views":, yt.views)