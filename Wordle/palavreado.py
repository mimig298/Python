from random import choice

with open("Assets/words_all.txt", "r") as file:
    words = file.read().split("\n")

def check(guess):
    correct = True
    if len(guess) < 2 and guess != [""]:
        print("Input missing either the guessed word, results, or a whitespace.")
        correct = False
    elif len(guess) > 2:
        print("Input too long. Only two words separated by a single whitespace are accepted.")
        correct = False
    for wordy in range(len(guess)):
        word = guess[wordy]
        if len(word) != 5 and guess != [""]:
            print(f"Only 5-letter words are accepted, but '{word}' is {len(word)} letters long.")
            correct = False
        if wordy == 1:
            for char in word:
                if char.upper() not in ["G", "B", "Y"]:
                    print(f"Unexpected character '{char}' in results. Make sure only the letters 'G', 'B' and 'Y' are present.")
                    correct = False
    return correct

def analyze(letterdata, guess):
    guessdata = {}
    for car in range(len(guess[0])):
        char = guess[0][car].lower()
        if char not in guessdata.keys():
            guessdata[char] = [[], 0, False]
        guessdata[char][0].append([guess[1][car], car])
        if guess[1][car] != "B":
            guessdata[char][1] += 1
        else:
            guessdata[char][2] = True
    for letter in guessdata:
        if letter in letterdata.keys():
            if guessdata[letter][1] > letterdata[letter][1]:
                letterdata[letter][1] = guessdata[letter][1]
            for check in guessdata[letter][0]:
                if check not in letterdata[letter][0]:
                    letterdata[letter][0].append(check)
        else:
            letterdata[letter] = guessdata[letter]
    return letterdata

# letterdata[letter] = [[color, index], count, countmax?]
# countmax = am i sure that count is the same is in the answer?

def solve(words, letterdata):
    for letter in letterdata:
        check = letterdata[letter]
        if check[2]:
            correct1 = [word for word in words if word.count(letter) == check[1]]
        else:
            correct1 = [word for word in words if word.count(letter) >= check[1]]
        correct2 = correct1.copy()
        for hint in check[0]:
            if hint[0] in ["B", "Y"]:
                correct2 = [word for word in correct2 if word[hint[1]] != letter]
            elif hint[0] == "G":
                correct2 = [word for word in correct2 if word[hint[1]] == letter]
        print("Checked", letter, "\n", len(correct2), "/", len(correct1), "/", len(words), "words left")
        words = correct2
    return words

def answer(words):
    print("\n")
    if len(words) == 0:
        print("No solution found")
    elif len(words) < 10:
        print(words)
    else:
        print(choice(words))

letterdata = {}

while len(words) > 1:
    correct = False
    while not correct:
        newguess = input("\nInsert guess and results: ").split(" ")
        correct = check(newguess)
    if newguess != [""]:
        newguess[1] = newguess[1].upper()
        letterdata = analyze(letterdata, newguess)
        words = solve(words, letterdata)
    answer(words)
    print()

input()
