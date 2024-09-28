from moviepy.editor import VideoFileClip

# Video dosyasının yolu
video_file = "stt.mp4"
# Çıkarılacak ses dosyasının adı
audio_file = "audio.mp3"

# Video dosyasını yükle
video_clip = VideoFileClip(video_file)
# Sesi çıkar
audio_clip = video_clip.audio
# Sesi dosyaya kaydet
audio_clip.write_audiofile(audio_file)

print(f"Audio extracted and saved to {audio_file}")
