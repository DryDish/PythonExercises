# Using a list comprehension create a list of tuples from the folowing datastructure
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}

dict_original = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}

tuple_of_items = dict_original.items()
list_of_items = list(tuple_of_items)

print(f"List of tuples: {list_of_items}")
