# Ex 6: Extract .py files
#
# Create a commandline utility (program) that when run takes 1-3
#   commandline arguments where:

# * the first is the name of a directory in play
# * the second (optional) is a –flag (–todir <dirname>) that specifies where
#       the files in that directory should be copied to
# * the third (optional) is a –flag (–zip <filename>) that specifies if the
#       files should be zipped and what the zip file should be called.

# So if you run the program like this
#  python extract.py . --todir /tmp/ --zip archive.zip
#  you should copy all files in the current directory (.)
#  to a new tmp directory and the .py files should be put
#  in a zip folder names archive.zip

import sys
import os
import shutil
from zipfile import ZipFile


def get_folder_contents(folder_name):
    try:
        folder_contents = os.scandir(folder_name)
    except FileNotFoundError:
        return -1
    folders = []
    files = []
    for item in folder_contents:
        if item.is_file():
            text = str(item).rsplit('\'')
            files += [text[1]]
        if item.is_dir():
            text = str(item).rsplit('\'')
            folders += [text[1]]

    sorted_list = sorted(folders) + sorted(files)
    return sorted_list


def get_folder_contents_files(folder_name):
    try:
        folder_contents = os.scandir(folder_name)
    except FileNotFoundError:
        return -1
    files = []
    for item in folder_contents:
        if item.is_file():
            text = str(item).rsplit('\'')
            files += [text[1]]
    return sorted(files)


def main(input):
    from_folder_name = sys.argv[1]
    files = get_folder_contents(from_folder_name)
    if (files == -1):
        print("No files found in folder. Please select a new one.")
        return -1
    to_dir = ""
    print(len(sys.argv))
    if len(sys.argv) < 4:
        print("Insufficient arguments passed\n"
              "Usage: exercise6.py [start foldername]"
              " {--tofolder [foldername]} {--zip [zipname.zip]} ")
        return -1
    if sys.argv[2] == "--todir" and len(sys.argv) < 5:
        to_dir = sys.argv[3]
        files_new_dir = get_folder_contents(to_dir)
        if (files_new_dir == -1):
            print("Folder does not exist, please point to a real folder")
            return -1
        if (any(item in files for item in files_new_dir)):
            print("file(s) already exists in chosen directory.")
            return -1
        print(to_dir)
        files = get_folder_contents_files(from_folder_name)
        for item in files:
            print("item: ", item)
            shutil.copy(item, to_dir)
        print("Files copied successfully")
        return 0

    if "--zip" in sys.argv:
        zip_name = ""
        try:
            zip_name = sys.argv[-1]
        except Exception:
            print("Please provide a name for your zip file."
                  " It must end in '.zip'")
            return -1
        if zip_name == "" or zip_name == "--zip":
            print("Please provide a name for your zip file."
                  " It must end in '.zip'")
            return -1
        if not (zip_name.endswith(".zip")):
            print("Please make sure your file name ends with the suffix .zip")
            return -1
        try:
            zip_file = ZipFile(str(zip_name), 'x')
        except Exception:
            os.remove(zip_file)
            zip_file = ZipFile(str(zip_name), 'x')
        # exists = str([x for x in files if (x.find(zip_name) > -1)])
        # if (exists != "[]"):
        #    print("file already exists, please chose a new file name")
        #    return-1
        if sys.argv[2] == "--todir" and len(sys.argv) > 5:
            to_dir = sys.argv[3]
        else:
            to_dir = from_folder_name
        print("from:", from_folder_name)
        print("to:", to_dir)
        print("zip name:", zip_name)
        files = get_folder_contents_files(from_folder_name)
        print(files)
        for item in files:
            print(item)
            if item != zip_name:
                zip_file.write(item)
        if to_dir != ".":
            exists = []
            files = get_folder_contents(to_dir)
            exists = str([x for x in files if (x.find(zip_name) > -1)])
            print(exists)
            if (exists != "[]"):
                print("file already exists, please chose a new file name")
                return-1
            shutil.move(zip_name, to_dir)
            print("File(s) zipped and moved successfully")
            return 0
        zip_file.close()

    print("File(s) zipped successfully.")
    return 0


main(sys.argv[1::])
