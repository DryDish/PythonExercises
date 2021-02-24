import sys


def main(name):

    if name == 'alice' or name == 'jens':
        print("hello " + name)

    else:
        print('You are not real')


main(sys.argv[1])
