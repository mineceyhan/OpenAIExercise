import openai
import os
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv()

# Now you can access your variables
openai_api_key = os.getenv("OPENAI_API_KEY")

#Chat Completion API  and Completion API

#Completion API
response_creative = openai.ChatCompletion.create(
    model = 'gpt-4o-2024-05-13',
    messages = [
        {
            "role": "system",
            "content":  "Sen yaratıcı bir yazarsın."
        },
        {
            "role": "user",
            "content": "İnsanların Mars'ta yaşadığı bir gelecek hakkında bir bilim kurgu hikayesinin başlangıcını yaz."
        }
        ],
    top_p = 0.9, #   (Nucleus Sampling)(float):
        # Çekirdek örnekleme olarak bilinen bir teknik kullanır. 0 ile 1 arasında bir değer alır.
        # Model, yanıt üretirken en olası tokenların toplam olasılığı bu değere ulaşana kadar tokenları seçer.
    max_tokens = 15,  #(integer):
    #     Yanıtın içerebileceği maksimum token sayısını belirtir. Bu, yanıtın uzunluğunu kontrol etmeye yardımcı olur.
    temperature = 0.9, #temperature (float):
        # Yanıtların rastgeleliğini kontrol eder. 0 ile 2 arasında bir değer alır.
        # Düşük değerler daha deterministik ve tutarlı yanıtlar üretirken, yüksek değerler daha çeşitli ve yaratıcı yanıtlar üretir.
    n= 1, # (integer):
        # Üretilen yanıtların sayısını belirtir. Bu, aynı prompt için birden fazla yanıt almak istediğinizde kullanılır.
    presence_penalty = 0.5, #(float):
        # -2.0 ile 2.0 arasında bir değer alır. Belirli kelimelerin yanıt içinde tekrar edilme olasılığını kontrol eder. 
        # Pozitif değerler yeni konuların keşfedilmesini teşvik ederken,
        # negatif değerler belirli kelimelerin tekrar edilmesini teşvik eder.
    frequency_penalty = 0.5, # (float):
        # -2.0 ile 2.0 arasında bir değer alır. Aynı kelimenin yanıt içinde tekrar edilme sıklığını kontrol eder.
        # Pozitif değerler kelime tekrarlarını azaltırken, negatif değerler tekrarları artırır.
    stop=None, #(list or string):
        # Yanıtın durması gereken token veya token dizilerini belirtir.
        # Bu, belirli bir karakter dizisiyle karşılaşıldığında yanıtı durdurur.
)
print("Creative Response:")
print(response_creative)

response_deterministic = openai.ChatCompletion.create(
    model = 'gpt-4o-2024-05-13',
    messages = [
        {
            "role": "system",
            "content":  "Sen yaratıcı bir yazarsın."
        },
        {
            "role": "user",
            "content": "İnsanların Mars'ta yaşadığı bir gelecek hakkında bir bilim kurgu hikayesinin başlangıcını yaz."
        }
        ],
    top_p = 0.3, #   (Nucleus Sampling)(float):
    #max_tokens = 50,  #(integer):
    temperature = 0.3, #temperature (float):
    n= 1, # (integer):
    presence_penalty = 0.5, #(float):
    frequency_penalty = 0.5, # (float):
    stop=None, #(list or string):
)
print("Deterministic Response:")
print(response_deterministic)