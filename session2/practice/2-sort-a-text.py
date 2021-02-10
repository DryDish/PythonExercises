
def sortastring(text):
    for i in range (len(text)):
        if text[i] in "aeiouAEIOU":
            text = text.replace(text[i],"ø")

    text = text.replace("ø", '')
    text = sorted(text)
    return list(text)


string = "fully automated word shit"

print(sortastring(string))
