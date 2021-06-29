import time
import functools


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


# Store returned function in a variable
speak_func = get_speak_func(.5)
# Call stored function
speak_func("hello there")

# OR call returned function directly like so
get_speak_func(1)("there hello")

print(get_speak_func(1)("there hello"))
print(speak_func("hello there"))

print("-----------------------------------")
print("Decorators")
print("-----------------------------------")


#  Function that takes another function as a parameter
def func_timer(function):
    # Wrapper inner function that accepts any amount of arguments
    def wrapper(text):
        time_start = round(time.time() * 1000)
        function(text)
        timer_end = round(time.time() * 1000)
        print("execution time (ms): ", timer_end - time_start)
    # Returns the wrapper (functionality, function, functionality)
    return wrapper


def speak(words="whoops"):
    print(words)


# Basic
timed_speak = func_timer(speak)

timed_speak("Kawabunga")


# Pie syntax or annotation
#  Function that takes another function as a parameter
def func_timer(function):
    # Wrapper inner function that accepts any amount of arguments
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        time_start = round(time.time() * 1000)
        value = function(*args)
        timer_end = round(time.time() * 1000)
        print("execution time (ms): ", timer_end - time_start)
        return value  # return any value that function might make
    # Returns the wrapper (functionality, function, functionality)
    return wrapper


@func_timer
def speak(words="whoops"):
    print(words)


speak("Kahoot!")
