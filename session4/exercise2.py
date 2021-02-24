# Ex 2: Clothes List Comprehension
#
# (1)
# From 2 lists, using a list comprehension, create a list containing:
# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]
# colors = ['Black', 'White']
# sizes = ['s', 'm', 'l', 'xl']
#
# (2)
# If the tuple pair is in the following list, it should not be added to the comprehension generated list.
# soled_out = [('Black', 'm'), ('White', 's')]

print(" From 2 lists, using a list comprehension, create a list containing:")
print("[(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]")

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

print("Printed list:\n", [(color, size) for color in colors for size in sizes])
