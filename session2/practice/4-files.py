#!/usr/bin/python3
# Create a file and call it lyrics.txt (it does not need to have any content)
# Create a new file and call it songs.docx and in this file write 3 lines
#   of text to it.
# Open and read the content and write it to your terminal
#   window. * you should use the read(), readline(), and readlines()
#   methods for this. (so 3 times the same output).

# from typing import TextIO


songs_dox = "../files/songs.docx"


def separator(text):
    print(f"\n#----- Reading from songs.docx with {text} -----#\n")


lyricsFile = open("../files/lyrics.txt", "w+")
print("lyrics.txt has been created in folder files,",
      "any previous data has been deleted")
lyricsFile.close()

songsFile = open(songs_dox, "w+")

songsFile.write("This is the first line of the file.\n")
songsFile.write("And this is the second line of the file.\n")
songsFile.write("Ths is the third and final line of the file,",
                "I hope you enjoyed your stay.\n")
print("songs.docx has been created and overwritten")
songsFile.close()


# read()
separator("read()")
songsFile = open(songs_dox, "r")
if songsFile.mode == "r":
    text = songsFile.read()
    print(text)
songsFile.close()

# readline()
separator("readline()")
songsFile = open(songs_dox, "r")
if songsFile.mode == "r":
    text = songsFile.readline()
    while text:
        # printline adds a \n char so i want to remove my old one
        print(text.replace("\n", ""))
        text = songsFile.readline()
songsFile.close()

# readlines()
separator("readlines()")
songsFile = open(songs_dox, "r")
if songsFile.mode == "r":
    text = songsFile.readlines()
    for x in text:
        x = x.replace("\n", "")
        print(x)
songsFile.close()
