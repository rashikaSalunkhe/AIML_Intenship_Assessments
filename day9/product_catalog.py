import pandas as pd

# Create Series
products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

# Print full series
print("Full Series:")
print(products)

# Access price using label-based indexing
print("\nPrice of Laptop:")
print(products['Laptop'])

# Slice using positional indexing
print("\nFirst two products:")
print(products.iloc[0:2])
