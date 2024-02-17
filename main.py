from pytube import YouTube

def Download(link):
    youtubeDonwloadVideo = YouTube(link)
    youtubeDonwloadVideo = youtubeDonwloadVideo.streams.get_highest_resolution()
    try:
        youtubeDonwloadVideo.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)