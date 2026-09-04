# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def get_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")



# s1 = Student("Zeus", 20, 500)
# s2 = Student("Rahul", 24, 800)

# s1.get_info()
# s2.get_info()


# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposite(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance: {self.balance}")
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdraw. new balance: {self.balance}")


# amount = BankAccount("Zeus", 1000)
# amount.deposite(500)
# amount.withdraw(2000)
# amount.withdraw(800)



# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model


# car1 = Car("BMW", "X5")
# car2 = Car("Mercedes", "E-Class")


# print(car1.brand, car1.model)
# print(car2.brand, car2.model)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hello my name is {self.name} and i am {self.age} years old")

    
# p1 = Person("Zeus", 20)
# p2 = Person("Rahul", 20)

# p1.introduce()
# p2.introduce()


# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance


#     def check_balance(self):
#         print(f"Current Balance : {self.balance}")

# s1 = BankAccount(1000)
# s1.check_balance()




# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# r1 = Rectangle(10, 20)
# print(f"Area : {r1.area()}")
# print(f"Perimeter : {r1.perimeter()}")



# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no


#     def get_info(self):
#         print(f"Name: {self.name}, Roll No: {self.roll_no}")


# s1 = Student("Zeus", 20)
# s2 = Student("Rahul", 24)
# s3 = Student("Aman", 26)

# students_list = [s1, s2, s3]

# for student in students_list:
#     student.get_info()


# class Book:
#     def __init__(self, title, author, is_available):
#         self.title = title
#         self.author = author
#         self.is_available = is_available

#     def borrow_book(self):
#         if self.is_available:
#             self.is_available = False  
#             print(f"Book '{self.title}' successfully borrow ho gayi.")
#         else:
#             print(f"Sorry, '{self.title}' abhi available nahi hai.")
    
#     def return_book(self):
#         if not self.is_available:
#             self.is_available = True 
#             print(f"Book '{self.title}' successfully return ho gayi.")
#         else:
#             print(f"Book '{self.title}' pehle se hi library mein available hai.")


# b1 = Book("Python", "Zeus", True)
# b2 = Book("Java", "Rahul", False)
# b3 = Book("Ruby", "Amit", False)
# b4 = Book("Javacript", "Kaushal", True)
# b5 = Book("Rust", "Vikash", True)

# b1.borrow_book()
# b1.borrow_book()



