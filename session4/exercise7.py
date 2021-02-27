# Ex 7: Simple scraper with requests

# 1. Create an application that asks for an url.

# 2. Then Download that html page, and its images, icons etc. and change it
#   so it will work locally on your computer. Locally means that you
#   should be able to cut your internet connection and still have
#   a functioning html page.

# 3. When done push all files to you github account. (you are allowed
#   to manually create an online repo and feed the clone url to your program.
#   but the rest should be done through python).

# You will have to use the requests module, the OS module
#   and the subprocesses module for this task.

import requests


def main():
    # url = input("Please type a url you would like to download:\n")
    url = 'https://www.python.org'
    try:
        request = requests.get(url)
        request.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Invalid URL, please try something else.")
        return -1
    print(request.status_code)

    return 0


main()
