

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
# print("translate red", translate["white"])

# user = {
#     "first_name": "Robert",
#     "last_name": "Smith",
#     "age": 19,
#     "school": {
#         "school_name": "Fresno State",
#         "grade": "senior",
#         "gpa": 3.5,
#         "completed_courses": [
#             "Programing Fund",
#             "Project Management"
#             "Psychology"
#         ]
#     }
# }

# # print("Lengthof dictionart: ", len(user))
# # print(user["first_name"] + "age is: ", user["age"])
# # print("courses", user["school"]["completed_courses"])

# # #Robert goes to Fresno State and is taking 2 classes.
# # num_courses = len(user["school"]["completed_courses"])
# # output = user["first_name"] + "goes to" + user["school"]["school_name"] + "and is taking" + num_courses + str(num_courses) 

# # print(output)

# # if "school" in user:
# #     print("true")
# # else:
# #     print("false")


# # print["Original user: ", user]
# # user["school"] = None
# # print("Mutated user: ", user)


# original_dic = {}
# dict1 = {
#     "a": "A",
#     "b": "B",
#     "c": "C"
# }

# dict2 = {
#     "c": "C",
#     "d": "D",
#     "e": "E"
# }

# dict3 = {
#     "f": "F",
#     "g": "G",
#     "h": "H"
# }

# dict1.update(dict2)
# dict1.update(dict3)
# print("dict1", dict1)



def main():
    textese_dict = create_dictionary("textese.txt")
    prompt = ("Enter a simple sentence in lowercase letters without any punctuation")
    sentence = input(prompt)
    translate(sentence, textese_dict)


def create_dictionary(file_name):
    infile = open(file_name, "r") #"Textese.txt"
    text_list = [ line.rstrip()for line in infile ]
    infile.close()
    output = [x.split(",") for x in text_list]
    return dict(output)

def translate(sentence, textese_dict):
    words = sentence.split()
    for word in words:
        print(textese_dict.get(word, word) + " ", end="")

main()


