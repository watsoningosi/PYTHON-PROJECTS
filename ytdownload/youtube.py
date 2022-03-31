from pytube import YouTube
link = "https://youtu.be/0nWsmYnZX-M"
yt = YouTube(link)
yt.streams.first().download()