import requests
import os


def req():
    url = 'https://en.wikipedia.org/wiki/Name'
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
    for line in lines:
        print(line)
    html_text.close()


def make_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except Exception:
        print(f"Folder '{folder_name}' already exists. Using it for storage")
        return -1
    print(f"Folder '{folder_name}' created successfully")
    return 0


req()
