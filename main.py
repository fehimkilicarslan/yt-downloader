from pytube import YouTube


def downloadVideo(url):
    yt = YouTube(url)
    yt = yt.streams.get_highest_resolution()
    try:
        yt.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input('Enter the YouTube Video URL \n --> ')
downloadVideo(link)
