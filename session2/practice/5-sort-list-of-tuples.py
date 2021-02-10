#!/usr/bin/python3

# Sort Based on this list of tuples: 
#   [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
# Sort the list so the result looks like this: 
#   [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]

list_of_tuples = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5),(10,4),(10, 1),(3, 1)]

print(f"Unsorted list of tuples {list_of_tuples}")

list_of_tuples = sorted(list_of_tuples, key=lambda x: (x[-1],x[0]))

print(f"Sorted list of tuple {list_of_tuples}")