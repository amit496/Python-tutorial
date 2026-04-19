student = {
    "name": "Aman",
    "age": 15,
    "class": 10
}


print(student['age'])
print(student.get('class'))
print(student.get("marks", "Not Found"))

student["age"] = 17

student["marks"] = 85

print(student)


del student["marks"]
print(student)


for key in student:
    print(key,':- ' ,student[key])


# print('NEW')

# for key, value in student.items():
#     print(key, ":", value)


# for value in student.items():
#     print(key, ":::::", value)