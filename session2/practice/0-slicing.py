# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become ->
#   ['World', 'Huston', 'we', 'are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] ->
#   ['Hello', 'Huston', 'are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] ->
#   ['here', 'are', 'we', 'Huston', 'World', 'Hello']
# ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become ->
#   ['World', 'Huston', 'we', 'are']
# 'Hello World Huston we are here' -> 'World Huston we'

collection = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
collection1fixed = collection[1:5]
print(collection1fixed)

collection2fixed = collection[0:2]
print(collection2fixed)

collection3fixed = collection[4:6]
print(collection3fixed)

collection4fixed = collection[4:5]
print(collection4fixed)

collection5fixed = collection[0::2]
print(collection5fixed)

collection6fixed = collection[::-1]
print(collection6fixed)

collection7fixed = collection[::-1]
print(collection7fixed)

tuple1 = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
tuple1fixed = list(tuple1[1:])  # cast to list from tuple
print(tuple1fixed)

string = 'Hello World Huston we are here'
s = string[5:21]
print(s)
