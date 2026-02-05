# Raw list with duplicate user IDs
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# Convert list to set to remove duplicates
unique_users = set(raw_logs)

# Membership test
is_id05_present = "ID05" in unique_users
print("Is ID05 present?", is_id05_present)

# Count comparison
print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))

# Output the unique set
print("Unique User IDs:", unique_users)