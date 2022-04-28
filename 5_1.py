
file_name = "./infile.txt"
infile = open(file_name, 'r')

print("infile", infile)

# Can use this or not
# for line in infile: 
#     print("Line: ", line)

names = [line.rstrip() for line in infile]
print("names: ", names)

infile.close()


def main():
    display_with_forloop(file_name)

def display_with_forloop(file_name):
    infile = open(file_name, 'r')
    for line in infile:
        print(line, end="")
    infile.close()


def display_with_list_comprehension(file_name):
    infile = open(file_name, 'r')
    items = [line.rstrip() for line in infile]
    print("items: ", items) 
    infile.close()


def open_file(file_name, mode):
    return open(file_name, mode)


main()