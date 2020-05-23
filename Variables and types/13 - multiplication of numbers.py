#The program asks the user for a 3 integer
# Then multiply the first 2 numbers.
# Divide the result by 3 numbers.


a, b, c = input(('Enter 3 digits (separated by spaces): ')).split(" ")
print(f'Numbers entered: {a}, {b}, {c}')

firstNumber = int(a)
secondNumber = int(b)
thirdNumber = int(c)


multiplication = firstNumber * secondNumber
print(f'Multiplication result of 1 and 2 digits: {multiplication}')


division = multiplication / thirdNumber
print(f'Division result divided by 3 digits: {round(division, 2)}')