from random import choice

def GetList(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().split("\n")

def UpdateList(path, newlist):
    wordstring = ""
    for word in newlist:
        wordstring += word + "\n"
    with open(path, "w", encoding="utf-8") as file:
        file.write(wordstring[:len(wordstring)-1])

knownwords = ["word"] + GetList("../Assets/words_usable.txt")
words = GetList("../Assets/words_all.txt")

prev = ""
answr = ""
while True:
    if knownwords == words:
        print("All words done! :D")
        break
    if answr not in ["u", "s"]:
        chosen = "word"
        while chosen in knownwords:
            chosen = choice(words)
    print("\nDo you know the word " + chosen +"?")
    answr = ""
    while answr not in ["y", "n", "u", "s", "x"]:
        answr = input("[Y/N]: ").lower()
    if answr == "y":
        knownwords.append(chosen)
        print("Word kept (" + str(len(knownwords)-1) + "/" + str(len(words)) + " words)")
    elif answr == "n":
        words.remove(chosen)
        print("Word deleted (" + str(len(knownwords)-1) + "/" + str(len(words)) + " words)")
    elif answr == "u" and prev != "":
        if prev not in knownwords:
            words.append(prev)
        else:
            knownwords.remove(prev)
        print("Previous action undid successfully")
    elif answr == "s" and input("Save data to files? (cannot be undone!)\n[Y/N]: ").upper() == "Y":
        UpdateList("../Assets/words_all.txt", sorted(words))
        UpdateList("../Assets/words_usable.txt", sorted(knownwords[1:]))
        print("Word list updated successfully!")
    elif answr == "x":
        break
    prev = chosen

input()