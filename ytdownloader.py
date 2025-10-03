from pytube import YouTube

def download_audio(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()
    print("Audio downloaded.")


