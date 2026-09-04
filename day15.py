# JSON Basics

# import json

# data = {"name": "Aarav", "age": 24, "skills": ["Python", "Java"]}

# json_string = json.dumps(data, indent=4)
# print(json_string)


# json_data = '{"name": "Aarav", "age": 24}'
# python_dict = json.loads(json_data)
# print(python_dict["name"])


# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data)


# import requests
# import json
# import ipdb

# response = requests.get("https://api.github.com/users/octocat")

# if response.status_code == 200:
#     ipdb.set_trace()
#     data = response.json()
#     json_string = json.dumps(data, indent=4)
#     print(json_string)
# else:
#     print("Error fetching data:", response.status_code)


# import json

# dict = {"name": "Aarav", "age": 500, "skills": ["Python", "Java"]}


# with open("data.json", "w") as file:
#     json.dump(dict, file, indent=4)

# print("Data saved to data.json")

# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data)



import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    data = response.json()
    json_data = json.dumps(data, indent=4)
    print(json_data)
else:
    print("Error fetching data:", response.status_code)