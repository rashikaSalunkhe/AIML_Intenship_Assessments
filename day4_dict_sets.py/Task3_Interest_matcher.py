# Create sets of interests
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

# Intersection: common interests
common_interests = friend_a & friend_b

# Union: all unique interests
all_interests = friend_a | friend_b

# Difference: interests only friend_a has
unique_to_a = friend_a - friend_b

# Print results
print("Common Interests:", common_interests)
print("All Interests:", all_interests)
print("Interests only Friend A has:", unique_to_a)
