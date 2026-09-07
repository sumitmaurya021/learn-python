# num = 0
# if num > 5:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")



# num = 6
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# a,b,c = 10,25,15
# if a >= b and a >=c:
#     print("A is Greatest")
# elif b >= a and b >= c:
#     print("B is Greatest")
# else:
#     print("C is Greatest")


# year = 2000

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a leap year")


# a,b = 20,10

# if a >= b:
#     print("A is greater")
# else: 
#     print("B is greater")

    

# age = 18

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")


# a = 10
# b = 20

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)


# N = 5
# total = 0
# for i in range(1, N+1):
#     total += i
# print(total)


# N = 4
# fact = 1
# for i in range(1, N+1):
#     fact *= i
# print(fact)

# num = 1234
# reversed_number = 0

# while num > 0:
#     digit = num % 10
#     print(f"Digit Num: {digit}")
#     reversed_number = reversed_number * 10 + digit
#     num = num // 10
#     print(f"Reverse Number: {reversed_number}")
    
# num = 121
# original = num
# reversed_number = 0

# while num > 0:
#     digit = num % 10
#     reversed_number = reversed_number * 10 + digit
#     num = num // 10
# if reversed_number == original:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
    


# num = 11
# is_prime = True

# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

# print("Prime" if is_prime else "Not prime")
    


# n = int(input())

# if n % 2 != 0:
#     print("Weird")
# elif 2 <= n <= 5:
#     print("Not Weird")
# elif 6 <= n <= 20:
#     print("Weird")
# elif n > 20:
#     print("Not Weird")


# # n = int(input())

# # for i in range(n):
# #     print(i ** 2)


def is_leap(year):
    leap = False
    
    # Leap year logic:
    # 1. Year 4 se divisible hona chahiye aur 100 se divisible NAHI hona chahiye
    # 2. YA fir Year 400 se divisible hona chahiye
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))
