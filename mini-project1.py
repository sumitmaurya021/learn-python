contacts = [
    {"name": "Riya", "phone": "9876543210", "city": "Ahmedabad"},
    {"name": "John", "phone": "9876543211", "city": "Mumbai"},
    {"name": "Jane", "phone": "9876543212", "city": "Delhi"},
]

print("==== Contact Book ====")
for contact in contacts:
    print(f"Name: {contact['name']} | Phone: {contact['phone']} | City: {contact['city']}")

search_name = input("\nSearch contact by name: ").strip().title()
found = False

for contact in contacts:
    if contact['name'] == search_name:
        print(f"Found -> {contact}")
        found = True
        break

if not found:
    print(f"No contact found with the name {search_name}")