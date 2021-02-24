# From these 2 sets:
# {'a', 'e', 'i', 'o', 'u', 'y'}
# {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

list_a = {'a', 'e', 'i', 'o', 'u', 'y'}
list_b = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

answer= list_a.union(list_b)
print(f"Union Answer: {answer}")

answer= list_a.symmetric_difference(list_b)
answer_revised = "0"
print(f"Symmetric Difference Answer: {}")

answer= list_a.difference(list_b)
print(f"Difference Answer: {answer}")

answer= list_a.isdisjoint(list_b)
print(f"disjoint Answer: {answer}")

answer= list_a.intersection(list_b)
print(f"Bonus Intersection Answer: {answer}")