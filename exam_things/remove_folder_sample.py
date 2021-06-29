import sys
import os

# sys.argv[0] # file path from python3 -> testing.py <-- for example
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    if len(sys.argv) > 2:
        arg2 = sys.argv[2]
# we can use additional information from that to make clever functions


def remove_folder(**key):
    if key["arg1"] == "--rmdir" and arg2:
        try:
            os.rmdir(key["arg2"])
        except FileNotFoundError:
            print(f"folder with name '{arg2}'' does not exist")


if arg1 and arg2:
    print("arg", arg2)
    remove_folder(arg1=arg1, arg2=arg2)
else:
    print("Please type '--rmdir' followed by the folder name")
