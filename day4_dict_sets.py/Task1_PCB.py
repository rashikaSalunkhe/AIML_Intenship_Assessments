contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Suresh": "9988776655"
}

# Add a new contact
contacts["Neha"] = "9012345678"

# Update phone number of an existing contact
contacts["Ravi"] = "9999999999"

# Safe access using get()
existing_contact = contacts.get("Anita", "Contact not found")
non_existing_contact = contacts.get("Rahul", "Contact not found")

print("Lookup Existing Contact:", existing_contact)
print("Lookup Non-existing Contact:", non_existing_contact)

print("\nContact List:")
# Iterate and print all contacts
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")