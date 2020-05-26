# Create a simple game
# The user guesses a number from 0 to 20.
# The number is hidden in the program (np. secret_num = 5).

secretNum = 5
while True:
    num = int(input('Enter the number: 0 - 20: '))
    if num == secretNum:
        print('Guess the number. Congratulations! ! :)')
        break
    else:
        print('Try again ;)')