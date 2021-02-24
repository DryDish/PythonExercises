# Ex 4: Sys module exercise

# Create a commandline tool that checks if the required aguments are
#   present when you run the program, and if not tells you what is
#   missing to run the program.

# If you run python python script.py the program should print an error saying
#   Usage: python script.py [-it]{--rm} where the [] means required
#   and the {} means optional.

import sys


def check_args(args):
    # where the [] means required", and the {} means optional.
    usage_info = "Usage: python script.py [-it]{--rm}"
    x = len(args)
    if (x >= 4):  # check for anything after the required input
        if args[3] != "":
            print(usage_info)
            return -1
    if (x >= 3):  # check that the second arg matches
        if args[2] != "--rm":
            print(usage_info)
            return -1
    if (x >= 2):  # check that the first arg matches
        if args[1] != "-it":
            print(usage_info)
            return -1
    print("succes!")
    return 0      # if we get here then great success!


check_args(sys.argv)
