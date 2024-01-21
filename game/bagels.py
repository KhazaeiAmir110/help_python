import random

number = 3
max_add = 10

def bagels():
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(max_add))

        numGuesses = 1
        while numGuesses <= max_add:
            gues = ''
            while len(gues) != number or not gues.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                gues = input('> ')

            clues = get(gues, secretNum)
            print(clues)
            numGuesses += 1

            if gues == secretNum:
                break
            if numGuesses > max_add:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(number):
        secretNum += str(numbers[i])
    return secretNum


def get(guess, secretNum):
    print(secretNum)
    if guess == secretNum:
        return 'You got it'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    bagels()