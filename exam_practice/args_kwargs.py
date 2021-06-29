# Accepts a List
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


# Works, but needs a List to work
print(my_sum([1, 2, 3, 4]))


# Accepts positional *args (name args NOT required)
def my_sum(*args):
    result = 0
    for numbers in args:
        result += numbers
    return result


# No longer needs a List to work
print(my_sum(1, 2, 3, 4))


# Accepts **kwargs (name kwargs NOT required)
def my_sum(**kwargs):
    result = 0
    for numbers in kwargs.values():
        result += numbers
    return result


# Needs a key to work
print(my_sum(a=1, b=2, c=3, d=4))


# Combining positional arguments, args and kwargs
def text_combiner(name, job, *args, **kwargs):
    text = f"{name} is a {job}"
    if not args:
        text += "."
    if args:
        text += " and a "
        for variables in args:
            text += f"{variables}, "
        text = text[:-2] + "."
    if kwargs:
        text += " Also, "
        for extras in kwargs.values():
            text += f"{extras}, "
        text = text[:-2] + "."
    return text


print(text_combiner("Peter", "mechanic", "lover", "boat", a="buff", b="tone"))
