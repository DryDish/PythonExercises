# ['World', 'Huston', 'we', 'are']
['Hello', 'World', 'Huston', 'we', 'are', 'here']
['Hello', 'World', 'Huston', 'we', 'are', 'here']  # ['Hello', 'World']
['Hello', 'World', 'Huston', 'we', 'are', 'here']  # ['are', 'here']
['Hello', 'World', 'Huston', 'we', 'are', 'here']  # ['are']
['Hello', 'World', 'Huston', 'we', 'are', 'here']  # ['Hello', 'Huston', 'are']
# ['here', 'are', 'we', 'Huston', 'World', 'Hello']
['Hello', 'World', 'Huston', 'we', 'are', 'here']

x = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
# should become -> ['World', 'Huston', 'we', 'are']
y = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
z = 'Hello World Huston we are here'  # -> 'World Huston we'

print(x[1:-1])
print(x[3::2])
print(x[4:5])
print(x[::2])
print(list(y[1:-1]))
print(z[z.index("World"):z.index("are")])


def stringFucker(string):
    fixed_string = string.replace("a", "")
    fixed_string = fixed_string.replace("i", "")
    fixed_string = fixed_string.replace("o", "")
    fixed_string = fixed_string.replace("u", "")
    fixed_string = fixed_string.replace("e", "")
    fixed_string = fixed_string.replace(" ", "")
    return sorted(fixed_string)


def new_sorter(string):
    fixed_string = string
    for forbidden_char in ['a', "i", "o", "u", "e", " "]:
        fixed_string = fixed_string.lower().replace(forbidden_char, "")
    return sorted(fixed_string)


s = "here we go buoys so fucking hot a"
s.format()
print(stringFucker(s))
print(new_sorter(s))


names = ["Alex", "Peter", "Jensen", "Bea", "And so on", "Panda"]

print(sorted(names))
print(sorted(names, reverse=True))
print(sorted(names, key=len))
print(sorted(names, key=lambda x: x[-1]))


def find_fist_a(name):
    pos = name.lower().find("a")
    if pos == -1:
        pos = 999
    return pos


print(sorted(names, key=find_fist_a))

tuples_list = [(1, 2), (2, 2), (3, 2), (2, 1), (2, 2),
               (1, 5), (10, 4), (10, 1), (3, 1)]


def sort_order(tuple):
    return (tuple[1], tuple[0])


print(sorted(tuples_list, key=sort_order))

# Open file in write mode and write stuff
file = open("file.txt", "w")
file.writelines("Hello!\n")
file.writelines("my friend\n")
file.writelines("TEXT")
file.writelines("TEXT")
file.close()

# Open file in read mode and print the file
file = open("file.txt", "r")
print(file.read())
file.close()

# ... and print one line at a time, as long as there are lines
file = open("file.txt", "r")
text = file.readline()
while text:
    print(text)
    text = file.readline()
print(file.read())
file.close()

# ... and iterate through the returned array
file = open("file.txt", "r")
text = file.readlines()
for line in text:
    print(line)
file.close()
