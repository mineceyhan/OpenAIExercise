import whisper
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError


model = whisper.load_model('base')
yt_url = "https://www.youtube.com/watch?v=NT2H9iyd-ms"
yt = YouTube(yt_url)

try:
    streams = yt.streams
    for stream in streams:
        print(stream)
except AgeRestrictedError:
    print("This video is age-restricted.")
except Exception as e:
    print(f"An error occurred: {e}")