import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# File paths
file_path = r"files\Impact_of_Mobile_Phone_on_Students_Health.csv"

# Load dataset
df = pd.read_csv(file_path)
print(df)


from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

df['embedding_OS'] = df['Mobile Operating System '].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
# df.to_csv(file_path)
# df = pd.read_csv(file_path)
# print(df)

# Embedding'leri listeye çevir
embedding_matrix = np.array(df['embedding_OS'].tolist())

# t-SNE ile boyut indirgeme
tsne = TSNE(n_components=2,  perplexity=30, learning_rate=200, random_state=0)
reduced_embeddings = tsne.fit_transform(embedding_matrix)

# İndirgenmiş verileri DataFrame'e ekle
df['TSNE1'] = reduced_embeddings[:, 0]
df['TSNE2'] = reduced_embeddings[:, 1]

plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='TSNE1', y='Age', hue='Mobile Operating System ', palette='viridis', s=100)
plt.title('Mobile Operating System Embeddings Visualized with t-SNE')
plt.xlabel('TSNE1')
plt.ylabel('Age')
plt.legend(title='Operating System')
plt.show()
