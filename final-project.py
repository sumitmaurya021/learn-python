from random import randint
import json
import os

FILENAME = "students.json"

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def to_dict(self):
        return{
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks
        }

def load_students():
    if not os.path.exists(FILENAME):
        return []
    try: 
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_students(students):
    with open(FILENAME, 'w') as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Student ka name: ").strip().title()
    try:
        roll_no = int(input("Roll Number: "))
    except ValueError:
        print("Invalid roll number")
        return

    marks = {}
    num_subjects = int(input("Kitne subjects hai? "))
    for i in range(num_subjects):
        subject = input(f"Subject {i+1} ka naam: ").strip().title()
        try:
            score = float(input(f"{subject} mein marks: "))
            marks[subject] = score
        except ValueError:
            print("invalid marks, skip kar diya")
    
    student = Student(name, roll_no, marks)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)
    print(f"Student {name} add ho gaya hai")

def view_students():
    students = load_students()
    if not students:
        print("Koi student record nahi hai")
        return
    print("\n===== All Students =====")
    for s in students:
        avg = sum(s["marks"].values()) / len(s["marks"]) if s["marks"] else 0
        print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Average: {avg:.2f}")


def search_student():
    students = load_students()
    try:
        roll_no = int(input("Search karne ke liye roll number: "))
    except ValueError:
        print("Invalid input!")
        return

    found = [s for s in students if s["roll_no"] == roll_no]   # list comprehension!

    if found:
        s = found[0]
        print(f"Found -> Name: {s['name']}, Marks: {s['marks']}")
    else:
        print("Student nahi mila")


def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Dhanyawad! Program band ho raha hai.")
            break
        else:
            print("Invalid choice, dobara try karo")


if __name__ == "__main__":
    main_menu()

    
