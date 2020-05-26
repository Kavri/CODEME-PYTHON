# Write a game - ROCK (k) / PAPER (p) / SCISSORS (n).
# The user enters one of 3 figures.
# The computer draws one of three figures.
# Check who won the round..
# The user enters the number of rounds.

import random
import sys


print('GAME - ROCK PAPER SCISSORS')

playerScore = 0
compScore = 0

print('If you want to end game type "end".')
print('')
numberRounds = int(input('How many rounds will you play?? '))

for playerSelection in range(numberRounds) :

    playerSelection = input('CHOOSE THE FIGURE - ENTER THE LETTER: ROCK (r) / PAPER (p) / SCISSORS (s): ')
    playerSelection = playerSelection.lower()

    if playerSelection == 'end':
        print('Thank you for the game. :)')
        sys.exit(0)


    compSelection = random.randint(1,3)

    if compSelection == 1:
        compSelection = 'r'
    elif compSelection == 2:
        compSelection = 'p'
    else:
        compSelection = 's'

    if playerSelection == compSelection:
        print('DRAW')

    elif playerSelection == 'r' and compSelection == 'p':
        print('ROCK VS PAPER')
        print('DEFEAT')
        compScore +=  1

    elif playerSelection == 'r' and compSelection == 's':
        print('ROCK + SCISSORS')
        print('WIN')
        playerScore += 1

    elif playerSelection == 'p' and compSelection == 'r':
        print('PAPER VS ROCK')
        print('WIN')
        playerScore += 1

    elif playerSelection == 'p' and compSelection == 's':
        print('PAPER VS SCISSORS')
        print('DEFEAT')
        playerScore +=  1

    elif playerSelection == 's' and compSelection == 'r':
        print('SCISSORS VS ROCK')
        print('DEFEAT')
        compScore +=  1

    elif playerSelection == 's' and compSelection == 'p':
        print('SCISSORS VS PAPER')
        print('WIN')
        playerScore += 1

    else:
        print('Invalid parameter')

print('RESULTS')
print('YOUR RESULT:', playerScore)
print('OPPONENT RESULT', compScore)

if playerScore > compScore:
    print('WIN!')

elif playerScore < compScore:
    print('DEFEAT')
else:
    print('DRAW')

print('Thank you for the game. :)')