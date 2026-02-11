import numpy as np

# Create a 5x3 array of random student scores
scores = np.random.randint(50, 101, size=(5, 3))

# Calculate column-wise mean (subject-wise average)
mean_scores = scores.mean(axis=0)

# Subtract mean using broadcasting
centered_scores = scores - mean_scores

# Output
print("Original Scores:\n", scores)
print("\nMean of each subject:\n", mean_scores)
print("\nCentered (Normalized) Scores:\n", centered_scores)
