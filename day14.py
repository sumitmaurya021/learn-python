# class Animal:
#     def eat(self):
#         print("Animal is eating")
    

# class Dog(Animal):
#     def bark(self):
#         print("Barking...")

# d = Dog()
# d.eat()
# d.bark()


# squares = [x**2 for x in range(5)]

# squares = []

# for x in range(5):
#     squares.append(x**2)

# print(squares)


# square = lambda x: x**2
# print(square(5))

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# for number in count_up_to(5):
#     print(number)


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


#     def show_salery(self):
#         print(f"{self.name}s' salary: {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)

#         self.team_size = team_size

#     def show_team(self):
#         print(f"{self.name} manages {self.team_size} people")



# m = Manager("Rohan", 8000, 5)
# m.show_salery()
# m.show_team()


# numbers = [1, 2, 3, 4, 5, 6]

# squares = [n**2 for n in numbers]
# print(squares)   # [1, 4, 9, 16, 25, 36]

# evens = [n for n in numbers if n % 2 == 0]   # with condition
# print(evens)      # [2, 4, 6]

# square_dict = {n: n**2 for n in numbers}
# print(square_dict)   # {1: 1, 2: 4, 3: 9, ...}


# from functools import reduce

# numbers = [1,2,3,4,5]

# squared = list(map(lambda x: x**2, numbers))
# print(squared)


# evens  = list(filter(lambda x: x % 2 == 2, numbers))
# print(evens)

# product = reduce(lambda x, y: x * y, numbers)
# print(product)

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")


# class Car(Vehicle):
#     def __init__(self, brand, model, num_doors):
#         super().__init__(brand, model)
#         self.num_doors = num_doors

#     def display_info(self):
#         super().display_info()
#         print(f"Number of doors: {self.num_doors}")

# class Bike(Vehicle):
#     def __init__(self, brand, model, has_basket):
#         super().__init__(brand, model)
#         self.has_basket = has_basket

#     def display_info(self):
#         super().display_info()
#         print(f"Has basket: {self.has_basket}")


# car = Car("Toyota", "Corolla", 4)
# bike = Bike("Hero", "Splendor", True)

# car.display_info()
# bike.display_info()


# Encapsulation use karke ek Account class banao jisme balance private ho.


# class Account:
#     def __init__(self, owner, balance):
#         self.__owner = owner
#         self.__balance = balance

#     def deposite(self, amount):
#         self.__balance += amount
#         print(f"Deposited {amount}. New balance: {self.__balance}")

#     def get_balance(self):
#         return self.__balance
    
#     def withdraw(self, amount):
#         if amount:
#             self.__balance -= amount
#             print(f"Withdrawn {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid amount")


# acc = Account("Amit", 5000)
# acc.deposite(2000)
# print(acc.get_balance())
# acc.withdraw(1000)
# print(acc.get_balance())


# List comprehension se 1-50 mein sirf prime-check ke bina, multiples of 5 nikaalo.


# multiples_of_5 = [i for i in range(1, 51) if i % 5 == 0]
# print(multiples_of_5)

# # Dict comprehension se ek list of words ki length ka dictionary banao.

# words = ["apple", "banana", "cherry", "date", "elderberry"]
# word_lengths = {word: len(word) for word in words}
# print(word_lengths)


# # lambda aur map() use karke ek list ke saare numbers ko double karo.

# numbers = [1,2,3,4,5,6,7,8,9]

# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)


# # Generator function banao jo Fibonacci series generate kare.

# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b


# for number in fibonacci(20):
#     print(number, end=" ")
    


# class Shape:
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14159 * self.radius * self.radius




# # Generator se 1 se 10 tak square print karo (no list).

# def squares(n):
#     for i in range(1, n+1):
#         yield i**2


# for number in squares(10):
#     print(number, end=" ")


# # Lambda aur map() se ek list ke sabhi numbers ko cubes banao

# numbers = [1,2,3,4,5,6,7,8,9,10]

# cubes = list(map(lambda x: x**3, numbers))
# print(cubes)


