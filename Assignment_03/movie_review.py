import pandas as pd
import numpy as np

# Read the dataset
data = pd.read_csv('moviereviews.csv')

# Calculate movie review vectors
movie_reviews = data.pivot_table(index='movie', columns='review', aggfunc='size', fill_value=0)
movie_vectors = movie_reviews.values

# Find similarity using dot product and angle between vectors
def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    epsilon = 1e-8
    if norm_v1 == 0 or norm_v2 == 0:
        return 0
    
    cosine_sim = dot_product / (norm_v1 * norm_v2)
    return cosine_sim

num_movies = movie_vectors.shape[0]
similarities = np.zeros((num_movies, num_movies))

print("Movie Vectors:")
print(movie_vectors)

for i in range(num_movies):
    for j in range(i, num_movies):
        similarity = cosine_similarity(movie_vectors[i], movie_vectors[j])
        similarities[i, j] = similarity
        similarities[j, i] = similarity

print("Similarities:")
print(similarities)

# Identify top 3 pairs of movies that are very much alike
top_pairs = []
for i in range(num_movies):
    for j in range(i+1, num_movies):
        top_pairs.append((data['movie'][i], data['movie'][j], similarities[i, j]))

top_pairs.sort(key=lambda x: x[2], reverse=True)
top_pairs = top_pairs[:3]

for pair in top_pairs:
    print(f"Movies: {pair[0]}, {pair[1]}, Similarity: {pair[2]:.4f}")

