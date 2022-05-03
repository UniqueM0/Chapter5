

from fnmatch import translate


translate = {
    "red": "rojo",
    "blue": "aloz",
    "green": "verdi",
    "white": "blanco"
}

# alist = [
#     "rojo",
#     "aloz",
#     "verdi",
#     "blanco"
# ]
# print("alist", alist[1])
print("translate red", translate["white"])

user = {
    "first_name": "Robert",
    "last_name": "Smith",
    "age": 19,
    "school": {
        "school_name": "Fresno State",
        "grade": "senior",
        "gpa": 3.5,
        "completed_courses": [
            "Programing Fund",
            "Project Management"
            "Psychology"
        ]
    }
}

# print("Lengthof dictionart: ", len(user))
# print(user["first_name"] + "age is: ", user["age"])
# print("courses", user["school"]["completed_courses"])

# #Robert goes to Fresno State and is taking 2 classes.
# num_courses = len(user["school"]["completed_courses"])
# output = user["first_name"] + "goes to" + user["school"]["school_name"] + "and is taking" + num_courses + str(num_courses) 

# print(output)

# if "school" in user:
#     print("true")
# else:
#     print("false")


print["Original user: ", user]
user["school"] = None
print("Mutated user: ", user)