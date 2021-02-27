# Ex 5: OS Module exercise
# Do the following task using the os module

# 1. create a folder and name the folder 'os_exercises.'
# 2. In that folder create a file. Name the file 'exercise.py'
# 3. get input from the console and write it to the file.
# 4. repeat step 2 and 3 (name the file something else).
# 5. read the content of the files and and print it to the console.

import os


def initialize_folder_and_file(folder_name, file_name):
    try:
        os.remove(folder_name + '/' + file_name)  # delete file if exists
    except FileNotFoundError:
        print("file not found for deletion")

    try:
        os.rmdir(folder_name)      # remove directory if exists
    except OSError:
        print("Folder was not empty")
    except FileExistsError:
        print("Folder was not found")

    os.mkdir(folder_name)          # make directory
    os.chdir(folder_name)          # navigate to new directory
    python_file_write = os.open(file_name, os.O_WRONLY | os.O_CREAT)
    return python_file_write       # return a file descriptor


def write_to_file(file_name):
    print("Please type something cool to go in the file\n"
          "When you are done typing write \\p")
    text = ""
    # keep saving input until the escape sequence is found
    while (text.count('\\q') < 1):
        text += input()
        text += "\n"
    text = text[0:-3]   # remove the escape sequence
    text += "\n"        # restore the new line at end of file
    os.write(file_name, text.encode('utf-8'))
    print("\n")
    os.close(file_name)
    os.chdir('..')


def read_from_file(folder_name, file_name):
    os.chdir(folder_name)
    print("This is the file's contents after reading from disk\n")
    file_read = os.open(file_name, os.O_RDONLY)
    text = str(os.read(file_read, 2048), 'utf-8')
    print(text)
    os.close(file_read)
    os.chdir('..')


def main():
    folder_name = ""
    file_name = ""

    folder_name = input("Please enter a folder name:\n")
    file_name = input("Please enter a file name\n")

    # assignment 1 & 2
    exercise_py = initialize_folder_and_file(folder_name, file_name)
    # assignment 3
    write_to_file(exercise_py)
    # assignment 4 & 5
    read_from_file(folder_name, file_name)

    # next file
    folder_name = input("Please enter a folder name:\n")
    file_name = input("Please enter a file name\n")
    file2_txt = initialize_folder_and_file(folder_name, file_name)
    write_to_file(file2_txt)
    read_from_file(folder_name, file_name)


main()
