import random

def takeGuess():
    print('Take a guess.')
    guess = int(input())
    global numberOfGuesses
    numberOfGuesses += 1

    if guess < answer:
        print('Your guess is too low')
        takeGuess()
    elif guess > answer:
        print('Your guess is too high')
        takeGuess()
    else: #guess == answer
        print('Good job, you guessed my number in ' + str(numberOfGuesses) + ' guesses!')

print('I am thinking about a number between 1 and 20.')
answer = random.randint(1,20)
numberOfGuesses = 0
takeGuess()