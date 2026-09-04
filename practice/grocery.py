item_name = input("Enter grocery name: ").strip().title()
item_amount = float(input("Enter the amount: "))
item_quantity = int(input("Enter you quantity: "))


total = item_amount * item_quantity

if total > 500:
    discount = total * 0.10
    total = total - discount
    print(f"{item_quantity} {item_name} ka bill: {total:.2f} (10% discount applied)")
else:
    print(f"{item_quantity} {item_name} ka bill: {total:.2f}")