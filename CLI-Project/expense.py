import json
import os

FILENAME = "expenses.json"

class Expense:
    def __init__(self, amount, category, data, description=""):
        self.amount = amount
        self.category = category
        self.data = data
        self.description = description


    def to_dict(self):
        return{
            "amount": self.amount,
            "category": self.category,
            "data": self.data,
            "description": self.description,
        }


def load_expenses():
    if not os.path.lexists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount positive hona chahiye!")
            return
    except ValueError:
        print("Invalid amount! Sirf number daalo.")
        return

    category = input("Category (eg: Food, Travel, Rent): ").strip().title()
    date = input("Date (DD-MM-YYYY): ").strip()
    description = input("Description (Optional): ").strip()

    expense = Expense(amount, category, date, description)

    expenses = load_expenses()
    expenses.append(expense.to_dict())
    save_expenses(expenses)
    print(f"Expense added: {category} - {amount}")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("Koi expense record nhi hai.")
        return

    print("\n==== All Expenses ====")
    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. {exp['date']} | {exp['category']} | "
            f"{exp['amount']} | {exp[description]}"
            )


def category_summary():
    expenses = load_expenses()
    if not expenses:
        print("Koi expense record nahi hai.")
        return


    categories = {exp["category"]  for exp in expenses}
    summery = {
        cat: sum(exp["amount"] for exp in expenses if exp["category"] == cat)
        for cat in categories
    }

    print("\n==== Category-wise Summary ====")
    for cat, total in summery.items():
        print(f"{cat}: R {total}")

    print("\nTotal Spent: R{sum(summary.values())}")

def main_menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")

        choice = input("Choose an action: ").strip()


        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("Dhanyawad! Program band ho raha hai.")
            break
        else:
            print("Invalid choice, dobara try karo.")
        

if __name__ == "__main__":
    main_menu()
 