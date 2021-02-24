# Ex 3: List & tuple exercises
# Based on these exercises from last time, solve the exercises
# by using list comprehensions instead.
#
# List & tuple exercises


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    words = [(len(word) >= 2 and word[0] == word[-1]) for word in words]
    return words.count(True)


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    x = sorted([word for word in words if word[0] == 'x' or word[0] == 'X'])
    no_x = sorted([word for word in words if word[0] != 'x'
                  and word[0] != 'X'])

    return x + no_x


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

# example ([(1, 3), (3, 2), (2, 1)])
# old solution sorted(tuples, key=lambda x: x[-1])
def sort_last(tuples):
    return sorted([(tuple[0], tuple[-1]) if (len(tuple) < 3)
                  else (tuple[0], tuple[1], tuple[-1])
                  for tuple in tuples], key=lambda x: x[-1])


# D. Given a list of numbers, return a tuple where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns (1, 2, 3). You may create a new list or
# modify the passed in list.


def remove_adjacent(nums):
    return tuple([x for i, x in enumerate(nums) if nums[i] != nums[i-1]])


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    return sorted([x for x in list1 + list2])


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} got: {got} expected: {expected}')


# Calls the above functions with interesting inputs.

print('match_ends')
test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

print()
print('front_x')
test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
     ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
     ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
     ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

print()
print('sort_last')
test(sort_last([(1, 3), (3, 2), (2, 1)]),
     [(2, 1), (3, 2), (1, 3)])
test(sort_last([(2, 3), (1, 2), (3, 1)]),
     [(3, 1), (1, 2), (2, 3)])
test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
     [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

print()
print('remove_adjacent')
test(remove_adjacent([1, 2, 2, 3]), (1, 2, 3))
test(remove_adjacent([2, 2, 3, 3, 3]), (2, 3))
test(remove_adjacent([2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 5]), (2, 3, 5))
test(remove_adjacent([]), ())

print()
print('linear_merge')
test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
     ['aa', 'bb', 'cc', 'xx', 'zz'])
test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
     ['aa', 'bb', 'cc', 'xx', 'zz'])
test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
     ['aa', 'aa', 'aa', 'bb', 'bb'])
