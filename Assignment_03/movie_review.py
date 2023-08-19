# Import pandas and numpy
import pandas as pd
import numpy as np

# Read the data set
df = pd.read_csv("moviereviews.csv")

# Define a function to calculate the movie review vector
def movie_vector(movie):
  # Get the reviews for the movie
  reviews = df[df["movie"] == movie]["review"]
  # Initialize an empty vector of length 26 (one for each letter)
  vector = np.zeros(26)
  # Loop through the reviews
  for review in reviews:
    # Convert the review to lower case and remove punctuation
    review = review.lower().translate(str.maketrans("", "", ".,;:'\"?!"))
    # Loop through the letters in the review
    for letter in review:
      if "a" <= letter <= "z":
    # Increment the corresponding element in the vector by 1
        vector[ord(letter) - ord("a")] += 1
  # Return the vector
  return vector

# Define a function to calculate the similarity between two vectors using dot product and angle formulas
def similarity(v1, v2):
  # Calculate the dot product of the vectors
  dot = np.dot(v1, v2)
  # Calculate the magnitude of each vector
  mag1 = np.sqrt(np.sum(v1**2))
  mag2 = np.sqrt(np.sum(v2**2))
  # Calculate the cosine of the angle between the vectors
  cos = dot / (mag1 * mag2)
  # Return the similarity score (higher is more similar)
  return cos

# Get the unique movies in the data set
movies = df["movie"].unique()

# Initialize an empty list to store the pairs of movies and their similarity scores
pairs = []

# Loop through all possible pairs of movies
for i in range(len(movies)):
  for j in range(i + 1, len(movies)):
    # Get the movie names
    movie1 = movies[i]
    movie2 = movies[j]
    # Calculate their vectors
    v1 = movie_vector(movie1)
    v2 = movie_vector(movie2)
    # Calculate their similarity score
    score = similarity(v1, v2)
    # Append the pair and the score to the list
    pairs.append((movie1, movie2, score))

# Sort the list by descending order of similarity score
pairs.sort(key=lambda x: x[2], reverse=True)

# Print the top 3 pairs of movies that are very much alike
print("Top 3 pairs of movies that are very much alike:")
for i in range(3):
  print(f"{i + 1}. {pairs[i][0]} and {pairs[i][1]} with similarity score of {pairs[i][2]:.4f}")

