# try:
#     num = int(input("Number"))
#     result = 10 / num
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Enter only number, not latters")


# try: 
#     num = int(input("Number daalo: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Zero se devide nahi kar sakte hai Bro!")
# except ValueError:
#     print("Valid number nahi hai")
# else:
#     print(f"Success! Result: {result}")
# finally:
#     print("Program execution complete")


# def check_age(age):
#     if age < 0:
#         raise ValueError("Age nagative nahi ho sakta hai")
#     if age < 18:
#         raise Exception("Aap minor ho, entry allowed nahi")
#     return "Entry Allowe"


# try:
#     print(check_age(16))
# except ValueError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Error: {e}")

# try:
#     num1 = int(input("Pahla Number Daalo: "))
#     num2 = int(input("Doosara number daalo: "))
#     result = num1 % num2
#     print("Result", result)

# except ZeroDivisionError:
#     print("Zero se devide nahi kar sakte hai Bro!")



# list = [10, 20, 30, 40, 50]

# try:
#     index = int(input("Index daalo: "))
#     print(f"Element at index {index} is {list[index]}")

# except IndexError:
#     print(f"Index out of range hai bhai!")
# except ValueError:
#     print("Enter only number")



# dict = {"name": "zeus", "age": 20}

# try:
#     key = input("Key daalo: ")
#     value = dict[key]
#     print(f"{key}: {value}")

# except KeyError:
#     print("Ye key exist nahi karti!")


# num = int(input("Number enter karo: "))

# try: 
#     sum = 100 / num
#     print(f"Result: {sum}")
# except ZeroDivisionError:
#     print("Bro zero se devide nahi kar sakte hai!")
# else:
#     print("Try complete hua")
# finally:
#     print("Program execution completed!")

            
# try:
#     number1 = int(input("Pahla Number Daalo: "))
#     number2 = int(input("Doosara number daalo: "))
#     operation = input("Operation enter karo (Eg: +,-,*,/): ")

#     if operation == "+":
#         result = number1 + number2
#     elif operation == "-":
#         result = number1 - number2
#     elif operation == "*":
#         result = number1 * number2
#     elif operation == "/":
#         result = number1 / number2
#     else: 
#         result = "Invalid Operation"

#     print(f"Result: {result}")

# except ValueError:
#     print("invalid input: Enter valid numbers")
# except ZeroDivisionError:
#     print("cannot devide by zero")



