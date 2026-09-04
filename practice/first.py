# units = int(input("Total units consumed: "))

# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + (units - 100) * 7
# else:
#     bill = (100 * 5) + (100 * 7) + (units - 200) * 10


# print(f"Total Bill: {bill}")


name = input("Enter name: ")

for i in range(len(name)):
    print(name[i], end="")
    