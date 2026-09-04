expenses = []

for i in range(5):
    item = input(f"Item {i+1}  name: ")
    amount = float(input(f"{item} ka amount: "))
    expenses.append((item, amount))

total = sum(amount for item, amount in expenses)
costliest = max(expenses, key=lambda x: x[1])

print(f"\nTotal Expense: {total}")
print(f"Sabse mehenga item: \"{costliest[0]}\" ka amount {costliest[1]}")