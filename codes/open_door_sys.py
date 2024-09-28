import openai
import speech_recognition as sr
from dotenv import load_dotenv
import os
import httpx
import json
import pygame
import io

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def speech_to_text(audio_data):
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {
        'Authorization': f'Bearer {openai.api_key}',
    }
    files = {
        "file": ("audio.wav", audio_data, "audio/wav")
    }
    data = {
        "model": "whisper-1",
    }

    response = httpx.post(url, headers=headers, data=data, files=files)
    return response.json()

def text_to_speech(text_data):
    url = "https://api.openai.com/v1/audio/speech"
    headers = {
        'Authorization': f'Bearer {openai.api_key}',
    }

    content_data = json.dumps({
        "model": "tts-1",
        "input": text_data,
        "voice": "echo"
    })
    json_content = json.loads(content_data)
    try:
        resp = httpx.post(url=url, headers=headers, json=json_content, timeout=60)
        resp.raise_for_status()  # Ensure we catch HTTP errors
        # Verify content type
        if 'audio/mpeg' not in resp.headers.get('Content-Type', ''):
            raise ValueError("Invalid content type in response")
        # Use BytesIO to handle the audio data in memory
        audio_stream = io.BytesIO(resp.content)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_stream, 'mp3')
        pygame.mixer.music.play()
        # Keep the program running until the audio is finished
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"An error occurred: {e}")

def record_audio():
    recognizer = sr.Recognizer()
    
    # Adjust the recognizer's energy threshold
    recognizer.energy_threshold = 4000  # Adjust this value based on your environment
    
    with sr.Microphone() as source:
        print("Please say your name:")
        audio = recognizer.listen(source)
    
    audio_data = audio.get_wav_data()

    try:
        response = speech_to_text(audio_data)
        print(response)
        text = response['text'].strip()
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Collect safe names from user via console
def create_safe_user_list():
    text_to_speech("Please enter the safe names one by one.")
    safe_names = []
    for i in range(2):
        name = input(f"Enter safe name {i+1}: ").lower()
        safe_names.append(name)
    return safe_names

# User authentication
def authenticate_user(safe_names):
    text_to_speech("Please clearly say your name for verification.")
    user_name = record_audio()
    
    if user_name:
        user_name = user_name.lower()
        if user_name in safe_names:
            return True
        else:
            return False
    else:
        return False

# Main process flow
def main():
    print("Door Opening System")
    safe_names = create_safe_user_list()
    
    print("Now performing user authentication...")
    while True:
        if authenticate_user(safe_names):
            text_to_speech("Verification successful! The door is open.")
            return True
        else:
            text_to_speech("Verification failed! The door is closed.")

if __name__ == "__main__":
    main()
