import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
          
The order of clues does not provide any information they are alphabetically sorted

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        num = getNum()

        print('\n I have thought up a number. \n')
        print('You have {} guesses to get it. \n'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS:
                print('Guess #{}'.format(numGuesses))
                guess = input('->')

            clues = getClues(guess, num)
            print(clues)
            print('\n')
            
            numGuesses+=1

            if guess == num:
                break
            if numGuesses > MAX_GUESSES:
                print("Out of guesses")
                print("the correct answer was: ", num)
        
        print('Do you want to play again?')
        if not input('>>>').lower().startswith('y'):
            break
    print('Thanks for playing')

def getNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    num = ''
    for i in range(NUM_DIGITS):
        num+=str(numbers[i])
    return num

def getClues(guess, num):

    if guess==num:
        return 'You got it Right.'
    
    clues = []
    for i in range(NUM_DIGITS):
        if guess[i]==num[i]:
            clues.append('Fermi')
        elif  guess[i] in num:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()