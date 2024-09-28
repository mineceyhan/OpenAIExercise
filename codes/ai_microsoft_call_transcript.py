#Microsoft Earnings Call Transcript

import openai
import pandas as pd
import numpy as np
from getpass import getpass

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

file_path = 'microsoft-earnings.csv'
earnings_df = pd.read_csv('microsoft-earnings.csv')
print(earnings_df)

from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

earnings_df['embedding'] = earnings_df['text'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
earnings_df.to_csv('earnings-embeddings.csv')
while True:
    earnings_search = input("Search earnings for a sentence:") #artificial intelligence demand cloud products
    earnings_search_vector = get_embedding(earnings_search, engine="text-embedding-ada-002")
    earnings_df["similarities"] = earnings_df['embedding'].apply(lambda x: cosine_similarity(x, earnings_search_vector))
    print(earnings_df)
    print(earnings_df.sort_values("similarities", ascending=False))