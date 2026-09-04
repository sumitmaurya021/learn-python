# for i in range(1, 6):
#     print(f"Number: {i}")



# fruits = ["apple", "banana", "cherry", "date"]

# for fruit in fruits:
#     print(f"I like {fruit}.")


# count = 5

# while count > 0:
#     print(f"Countdown: {count}")
#     count -= 1
#     print("Liftoff!")



# for num in range(1, 100):
#     if num % 3 == 0:
#         print(f"Mila: {num}")
#         break


# for num in range(1, 10):
#     if num % 2 == 0:
#         continue
#     print(num)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"({i}, {j})", end=" ")
#     print()




# even number

# for i in range(1, 20):
#     if i % 2 == 0:
#         print(f"Even number: {i}")


# while loop se koi number entered hone tak (0 tak) sum calculate karo.



# total_sum = 0

# number = int(input("Enter a number (0 to stop):"))


# while number != 0:
#     total_sum += number
#     number = int(input("Enter a number (0 to stop)"))
#     print(f"Total sum: {total_sum}")



# for i in range(-5, 6):
#     if i < 0:
#         print(f"{i} is negative")
#     elif i == 0:
#         print(f"{i} is zero")
#     else:
#         print(f"{i} is positive")



# for i in range(1, 50):
#     if i % 3 == 0:
#         print(f"{i} is divisible by 3")


# Nested loop se ek simple star pattern print karo (triangle shape). 

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()



# number guessing game

# Ek "Number Guessing Game" banao — computer ek fixed number soche (e.g., 7), user while True loop mein guess kare, har galat guess pe "High" ya "Low" hint mile, aur sahi guess pe loop break ho jaye with attempts count.

# secret_number = 7
# user_number = int(input("Enter a number: "))
# attempts = 1

# while user_number != secret_number:
#     if user_number < secret_number:
#         print("Too Low!")
#     else:
#         print("Too High!")
    
#     user_number = int(input("Enter a number: "))
#     attempts += 1

# print(f"Correct! You guessed it in {attempts} attempts.")



