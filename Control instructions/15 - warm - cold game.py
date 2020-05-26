# Create a game - warm cold
# The computer draws a number - range from 1 to 100.
# User gives his luck.
# Computer responds warm - cold (up to 6 times)
# If the user guesses the number - win!

import random

print('GAME WARM COLD')
help = input('Do you want to see the rules of the game?? Enter YES / NO: ')
help = help.lower()

if help == 'yes':
    print('''1.The opponent draws a number - range from 1 to 100.
    2. You enter a number from 1 to 100. You have 6 tries..
    3. The opponent responds - warm cold.
    4. If you guess during 6 tries - win! :)
''')

else:
    print('')

revenge = 'yes'
while revenge == 'yes':

    choiceComp = random.randint(0, 100)

    for choicePlayer in range(6):
        choicePlayer = int(input('Enter the number: '))

        if choiceComp == choicePlayer:
            print('WIN')
            break

        if 1 <= choiceComp - choicePlayer <= 15:
            print('HOT')

        elif 16 <= choiceComp - choicePlayer <= 30:
            print('WARM')

        elif 31 <= choiceComp - choicePlayer <= 60:
            print('COLD')

        else:
            print('ICILY')
    print('')
    print('.' * 9)
    print('DEFEAT')
    print('The number drawn by the opponent:', choiceComp)
    revenge_1 = input('REVENGE? ENTER YES / NO: ')