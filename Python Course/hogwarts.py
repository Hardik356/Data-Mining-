# lists
students = ["Hermonine", "HArry", "ROn"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# range take numbers of list
# len - converts the studnets list in length 3 eg

# for i in range(len(students)):
#     print(i + 1 ,students[i])


# dictionaries keys and value  two dimensionla words with it s meaning

# students = ["Hermonine", "HArry", "ROn", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor","Slytherin"]

# students = { # key value pair
#     "Hermonine": "Gryffindor",
#     "HArry": "Gryffindor",
#     "ROn": "Gryffindor",
#     "Draco": "Slytherin",
# }


# for student in students:
#     print(student, students[student], sep=", ")


# list of dictionaores [ ] this gives list and {} this is dectionaries 
students = [
    {"name": "Hermonine", "house": "Gryffindor", "patron": "otter"},
    {"name": "HArry", "house": "Gryffindor", "patron": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patron": "jack russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patron": None}, # special keyword none absence of value 
]

for student in students :
    print(student["name"], student["house"], student["patron"], sep=", ")