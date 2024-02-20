import random
attempts = 0
num = random.randint(1, 100)
print('Guess a number between 1 and 100')
i = 0
while i != num:
    guess = input()
    attempts += 1
    i = int(guess)
    if i == num:
        print('You guessed right!')
        if attempts == 1:
            print('It took you ' + str(attempts) + ' attempt to guess the number! You are extremely lucky!')
        elif attempts <= 5:
            print('It took you ' + str(attempts) + ' attempts to guess the number! You are a pro at this!')
        elif attempts <= 10:
            print('It took you ' + str(attempts) + ' attempts to guess the number! You are good this!')
        elif attempts <= 15:
            print('It took you ' + str(attempts) + ' attempts to guess the number! Maybe you could try harder...')
        elif attempts <= 30:
            print('It took you ' + str(attempts) + ' attempts to guess the number! You really have some lack of skills.')
        elif attempts <= 60:
            print('It took you ' + str(attempts) + ' attempts to guess the number! You could REALLY do better.')
        elif attempts <= 90:
            print('It took you ' + str(attempts) + ' attempts to guess the number! You are either extremely unlucky or an idiot.')
        elif attempts > 90:
            print("It took you " + str(attempts) + " attempts to guess the number! Come on, you aren't even trying.")
    elif i < 1 or i > 100:
        print("That isn't even between 1 and 100. -1 point for that stupidity of yours.")
        attempts += 1
    elif i < num:
        print('Try higher')
    elif i > num:
        print('Try lower')
input()