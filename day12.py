# file = open("data.txt", "r")
# content = file.read()
# file.close()



# automatically closes the file
# with open("data.txt", "r") as file:
#     content = file.read()


# with open("data.txt", "w") as file:
#     file.write("Yeh mera pahla note hai.\n")
#     file.write("File handling seekh raha hoon.\n")


# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("data.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# with open("data.txt", "a") as file:
#     file.write("Ye naya line hai, purana data saaf hai.\n")

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)



# try:
#     with open("databb.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File nahi mila.")


# from contextlib import contextmanager
# with open("movies.txt", "w") as file:
#     file.write("3 IDIOTS - 2009\n")
#     file.write("SHOLAY - 1975\n")
#     file.write("MOTHER INDIA - 1957\n")
#     file.write("PK - 2014\n")
#     file.write("Dangal - 2016\n")


# with open("movies.txt", "r") as file:
#     movies = file.read()
#     list = movies.split("\n")
#     print(list)

# with open("movies.txt", "a") as file:
#     file.write("TAARE ZAMEEN PAR - 2007\n")

# with open("movies.txt", "r") as file:
#     movies = file.read()
#     list = movies.split("\n")
#     print(list)

# try:
#     with open("non.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File nahi mil rahi hai")

# with open("movies.txt", "r") as file:
#     movies = file.read()
#     print(len(movies))



with open("new.txt", "r") as file:
    content = file.read()
    print(content)


with open("new.txt", "a") as file:
    content = file.write(input("Enter your content: ") + "\n")


with open("new.txt", "r") as file:
    content = file.read()
    print(content)


delete = input("Delete this content: ")
with open("new.txt", "w") as file:
    file.write(content.replace(delete, ""))

with open("new.txt", "r") as file:
    content = file.read()
    print(content)