path = "../Assets/words_fiveletters.txt"

with open("../Assets/words_alpha.txt", "r") as file:
    allwords = file.read().split("\n")

newwords = []
for word in allwords:
    if len(word) == 5:
        newwords.append(word)

with open(path, "x") as file:
    for word in newwords:
        file.write(word+"\n")

print(len(newwords), "words added to", path)