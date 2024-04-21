from random import choice
from time import sleep

with open("Assets/words_usable.txt", "r", encoding="utf-8") as file:
    wordlist = file.read().split("\n")
correctword = choice(wordlist)

guesses = 0
guess = ""
while guesses < 6 and guess != correctword:
    guess = input()
    