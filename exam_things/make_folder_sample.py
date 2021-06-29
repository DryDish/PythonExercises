import sys
import os

# sys.argv[0] # file path from python3 -> testing.py <-- for example
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    if len(sys.argv) > 2:
        arg2 = sys.argv[2]
    else:
        print("Please add a folder name")
        exit()
# we can use additional information from that to make clever functions


def make_folder(**key):
    if key["arg1"] == "--mkdir" and arg2:
        try:
            os.mkdir(key["arg2"])
        except FileExistsError:
            print(f"folder with name '{arg2}'' already exists")


if arg1 and arg2:
    make_folder(arg1=arg1, arg2=arg2)
else:
    print("Please type '--mkdir' followed by the folder name")
