# Create a simple game
# The user guesses a number from 0 to 20.
# The number is hidden in the program (np. secret_num = 5).

secretNum = 5
variable = 0

while variable != secretNum:
    variable = int(input('Enter the number: 0 - 20: '))
    if variable == secretNum:
        print(f'Guess the number. Congratulations! The secret number is {secretNum}')
    else:
        if variable < 5:
            print('The number is bigger.')
        else:
            print('The number is smaller.')