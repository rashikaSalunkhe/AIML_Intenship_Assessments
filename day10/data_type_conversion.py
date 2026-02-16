import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders_type_conversion.csv")

# 1️⃣ Check data types before conversion
print("Before conversion:\n")
print(df.dtypes)

# 2️⃣ Convert price (remove $ and convert to float)
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# 3️⃣ Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# 4️⃣ Check data types after conversion
print("\nAfter conversion:\n")
print(df.dtypes)