# The program asks the user for 4 digits
# then returns the sum of the numbers

print("------------------ SUM OF NUMBERS ------------------")

a, b, c, d = input('Enter 4 digits (separated by spaces): ').split(" ")
print(f'Numbers entered: {a}, {b}, {c}, {d}')

firstNumber = int(a)
secondNumber = int(b)
thirdNumber = int(c)
fourthNumber = int(d)

total = firstNumber + secondNumber + thirdNumber + fourthNumber

print(f'Sum of numbers - {total}.')