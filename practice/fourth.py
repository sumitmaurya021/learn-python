email = input("Enter email: ").strip()

if "@" in email and "." in email and email.index("@") > 0:
    username, domain = email.split("@")
    print(f"Valid-looking email. Username: {username}, Domain: {domain}")
else:
    print("Invalid email format")