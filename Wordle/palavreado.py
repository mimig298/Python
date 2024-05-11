from random import choice

guesses = []
letterdata = {}

with open("puzzledata.txt", "r") as file:
    file = file.read().split("\n")
    for line in file:
        guesses.append(line.split(" "))

with open("Assets/words_all.txt", "r") as file:
    words = file.read().split("\n")

for guess in guesses:
    for char in range(len(guess[0])):
        letterdata[guess[0][char].lower()] = [guess[1][char].upper(), char]

for letter in letterdata:
    correct = []
    check = letterdata[letter]
    if check[0] == "G":
        for word in words:
            if word[check[1]] == letter:
                correct.append(word)
    elif check[0] == "B":
        for word in words:
            if letter not in word:
                correct.append(word)
    elif check[0] == "Y":
        for word in words:
            if letter in word and word[check[1]] != letter:
                correct.append(word)
    print("Checked", letter, "\n", len(correct), "/", len(words), "words left")
    words = correct

if len(words) < 50:
    print("\n", words)
else:
    print(choice(words))