import pandas as pd

# Create Series
grades = pd.Series([85, None, 92, 45, None, 78, 55])

# Print original
print("Original Series:")
print(grades)

# Identify missing values
print("\nMissing Values:")
print(grades.isnull())

# Fill missing values with 0
filled_grades = grades.fillna(0)
print("\nFilled Series (Missing replaced with 0):")
print(filled_grades)

# Filter scores greater than 60
filtered_grades = filled_grades[filled_grades > 60]
print("\nScores greater than 60:")
print(filtered_grades)