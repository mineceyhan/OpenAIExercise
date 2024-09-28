import openai
import os
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv()

# Now you can access your variables
openai_api_key = os.getenv("OPENAI_API_KEY")

response  = openai.ChatCompletion.create(
    model = 'text-davinci-003',
    messages = [
        {
            "role": "system",
            "content":  "Sen önceki kelimelere dayanarak sonraki kelimeyi tahmin eden bir botsun."
        },
        {
            "role": "user",
            "content": "Python bir ."
        }
        ],
        max_tokens=1,  # Tek kelime tahmini için
        n=1,  # Tek bir yanıt
        stop=None,
        temperature=0.7  # Çıktı çeşitliliği için
)
print(" Response:")
print(response)