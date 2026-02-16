import pandas as pd

# Create Series
usernames = pd.Series([' Alice ', 'bOB', 'Charlie_Data ', 'daisy'])

# Clean usernames
cleaned = usernames.str.strip().str.lower()

# Check which names contain letter 'a'
contains_a = cleaned.str.contains('a')

# Print results
print("Cleaned Usernames:")
print(cleaned)

print("\nContains letter 'a':")
print(contains_a)