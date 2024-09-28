import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
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

# Compute embeddings
df['embedding_OS'] = df['Mobile Operating System '].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))

# Convert embeddings to list
embedding_matrix = np.array(df['embedding_OS'].tolist())

# PCA ile boyut indirgeme
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embedding_matrix)

# İndirgenmiş verileri DataFrame'e ekle
df['PCA1'] = reduced_embeddings[:, 0]
df['PCA2'] = reduced_embeddings[:, 1]

# Grafik
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Mobile Operating System ', palette='viridis', s=100)
plt.title('Mobile Operating System Embeddings Visualized with PCA')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend(title='Operating System')
plt.show()
