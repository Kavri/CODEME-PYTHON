# The program asks the user for 2 digits
# then divides 1 digit by 2 digit
# How many times 1 number is in 2?
# What is the rest of dividing?

a, b = input('Enter 2 digits (separated by spaces): ').split(" ")
print(f'Numbers entered: {a}, {b}')

firstNumber = int(a)
secondNumber = int(b)

division = firstNumber / secondNumber
print(f'Division result: {round(division, 2)}')

division = int(division)

if division < 1:
    print('The first number only once fit in the second number.')
else:
    print(f'The first number will fit in the second - {division} times.')

restDivision= firstNumber % secondNumber
print(f'The rest of the division is {restDivision}.')