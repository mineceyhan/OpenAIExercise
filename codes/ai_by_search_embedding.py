#OpenAI Word Embeddings, Semantic Search  https://colab.research.google.com/drive/1tttDqgnWL9yJtmlOFXJqA-BjQ1Pyfpax?usp=sharing#scrollTo=CC0UgmJeCM36

import pandas as pd
import numpy as np
from getpass import getpass
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

file_path = r"C:\Users\ceyha\OneDrive\Masaüstü\openai\files\words.csv"
try:
    df = pd.read_csv(file_path)
    print(df)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when trying to access '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

from openai.embeddings_utils import get_embedding
df['embedding'] = df['text'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))  
# DataFrame'deki her bir metin (kelime veya cümle) için get_embedding fonksiyonunu uygular. lambda x: get_embedding(x, engine='text-embedding-ada-002') ifadesi, 
# her metni alır ve text-embedding-ada-002 modelini kullanarak embedding vektörünü hesaplar. Bu vektörler, df['embedding'] sütununa eklenir.
df.to_csv(file_path)
df = pd.read_csv(file_path) #CSV dosyasını tekrar okur ve DataFrame'e yükler. Bu, önceki adımda kaydedilen embedding vektörlerini içerir.       
df['embedding'] = df['embedding'].apply(eval).apply(np.array)
# words.csv dosyasındaki embedding sütunundaki her bir embedding vektörünü tekrar uygun bir formata dönüştürür.
    #eval: Bu fonksiyon, metin olarak saklanan embedding vektörlerini Python veri yapısına dönüştürür (örneğin, bir liste veya dizi).
    #np.array: Bu, embedding vektörlerini NumPy dizilerine dönüştürür, böylece matematiksel işlemler ve benzerlik hesaplamaları daha kolay yapılabilir.
print(df)

while True:
    search_term = input('Enter a search term: ')

    # semantic search
    search_term_vector = get_embedding(search_term, engine="text-embedding-ada-002")
    # print(search_term_vector)
    from openai.embeddings_utils import cosine_similarity

    df["similarities"] = df['embedding'].apply(lambda x: cosine_similarity(x, search_term_vector))
    print("similarities")
    print(df)

    sort  = df.sort_values("similarities", ascending=False).head(20)
    print("similarities sorting")
    print(sort)
    
    food_df = df.copy()

    milk_vector = food_df['embedding'][9]
    espresso_vector = food_df['embedding'][18]

    milk_espresso_vector = milk_vector + espresso_vector
    # milk_espresso_vector  

    from openai.embeddings_utils import cosine_similarity

    food_df["similarities"] = food_df['embedding'].apply(lambda x: cosine_similarity(x, milk_espresso_vector))
    sort = food_df.sort_values("similarities", ascending=False)  
    print("similarities")
    print(food_df["similarities"])
    print("sort")
    print(sort)
