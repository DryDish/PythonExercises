# Ex 1: Alphabet List Comprehensions
#
# Create a list of capital letters in the english alphabet
#
# Create a list of capital letter from the english aplhabet,
#   but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
#
# Create a list of capital letter from from the english aplhabet,
#   but exclude every second between F & O

print("Create a list of capital letters in the english alphabet")

start = ord('A')
end = ord('Z')

# +1 because the end of the range is not included in the range
capital_letters = [chr(x) for x in range(start, end+1)]
print(capital_letters)

# now in one line it would look like this:
# print([chr(x) for x in range(65, 91)])
