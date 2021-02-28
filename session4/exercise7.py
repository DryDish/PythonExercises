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
import os


def make_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except Exception:
        print(f"Folder '{folder_name}' already exists. Using it for storage")
        return -1
    print(f"Folder '{folder_name}' created successfully")
    return 0


def main():
    # url = input("Please type a url you would like to download:\n")
    url = 'https://en.wikipedia.org/wiki/Scrubber'
    # folder_name = input("Please type a folder name to"
    #                    " store the website into")
    folder_name = "test"
    make_folder(folder_name)
    os.chdir(folder_name)
    try:
        request = requests.get(url, allow_redirects=True)
        request.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Invalid URL, please try something else.")
        return -1
    print(request.status_code)
    html_file = open('web_page.html', 'wb')
    html_file.write(request.content)
    html_file.close()

    html_text = open('web_page.html', 'r')
    lines = html_text.readlines()
    html_text.close()

    extracted = []
    for line in lines:
        text = line.strip()
        index = text.find("<img")
        if index > 0:
            start_char = text.find("src=\"", index)
            start_char += 5
            end_char = text.find("\"", start_char)
            print(text[start_char:end_char])
            extracted.append(text[start_char:end_char])

    fixed_url = url.split('/')
    site_url = fixed_url[2]
    for img in extracted:
        print("fixed only:", site_url)
        print("images:", img)
        i = 0
        if not str(img).startswith('//'):
            img_url = "http://" + site_url + str(img)
            img_file = requests.get(img_url)
            image = open(f'image{i}.png', 'wb')
            image.write(img_file.content)
            image.close
            i += 1

    return 0


main()
