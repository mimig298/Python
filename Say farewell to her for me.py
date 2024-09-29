path = "C:/Program Files (x86)/Steam/steamapps/common/Celeste/Content/Dialog/English.txt"
string = "Say goodbye to her for me"
newstring = "Say farewell to her for me"

with open(path, "r", encoding="utf_8") as file:
    text = file.read()

if string in text:
    with open(path, "w", encoding="utf_8") as newfile:
        newfile.write(text.replace(string, newstring))
