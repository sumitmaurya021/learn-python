# numbers = {1,2,3,4,4,4,4,4,4}
# print(numbers)


# student ={
#     "name": "Sumit",
#     "age": 20,
#     "city": "Ahmedabad"
# }


# print(student)  

# print(student.get("nameee"))


# fruits_set = {"apple", "banana", "mango"}
# print(fruits_set)

# fruits_set.add("orange")
# print(fruits_set)


students = {
    "name": "Sumit",
    "age": 20,
    "marks": [90, 80, 70]
}

print(students["name"])
print(students.get("grade"))

students["grade"] = "A"
students["age"] = 21
print(students)

for key, value in students.items():
    print(key, value)