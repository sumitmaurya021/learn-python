
phone = input("Enter phone number: ").strip()


if len(phone) == 10 and phone.isdigit():
    masked = "X" * 6 + phone[-4:]
    print(f"Masked Number: {masked}")
else:
    print("Invalid Phone Number")