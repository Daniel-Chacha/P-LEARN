import yt_dlp


url=input('Enter the video url: ')

options={}
with yt_dlp.YoutubeDL(options) as x:
    x.download([url])

print('Video downloaded successfully')