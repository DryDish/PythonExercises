# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# Sort this list by using the sorted() build in function.
# Sort the list in reversed order.
# Sort the list on the length of the name.
# Sort the list based on the last letter in the name.
# Sort the list with the names where the letter ‘a’ is in the name first.

listOfNames = ["Banana", "Pear", "Cherry", "Aardvark", ]
print(f"Regular list of names: {listOfNames}")

sortedList = sorted(listOfNames)
print(f"Sorted list of names: {sortedList}")

invertedSort = sorted(listOfNames, reverse=True)
print(f"Invert+sorted list of names: {invertedSort}")

lengthSort = sorted(listOfNames, key=len)
print(f"Length sorted list of names: {lengthSort}")

lastLetterSort = sorted(listOfNames, key= lambda x: x[-1])
print(f"Sorted list of names by last letter: {lastLetterSort}")

def get_id_of_first_instance(x):
    print(x)
    index1 = x.find("a")
    index2 = x.find("A")
    if (index1 != -1 and index2 != -1):
        return min(index1,index2)

    if (index1 != -1):
        return index1

    if (index2 != -1):
        return index2

    return 999


byFirstA = sorted(listOfNames, key = get_id_of_first_instance)
print(f"Sorted list of names by first instance of a: {byFirstA}")
