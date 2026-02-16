import pandas as pd

# Sample dataset 
data = {
    "Location": [" New York", "new york", "NEW YORK ", "New York", "new york "]
}

df = pd.DataFrame(data)

print("Before Cleaning:")
print(df["Location"].unique())

# 1️⃣ Remove leading & trailing spaces
df["Location"] = df["Location"].str.strip()

# 2️⃣ Standardize casing (Title Case)
df["Location"] = df["Location"].str.title()

# 3️⃣ Verify result
print("\nAfter Cleaning:")
print(df["Location"].unique())
