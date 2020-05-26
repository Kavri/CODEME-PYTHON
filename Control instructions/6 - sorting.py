# Sorting.
# Create 3 variables - the user gives the digit to the variable
# Find the largest digit. Display number from smallest to largest.

a = input('Enter 1 digit:')
b = input('Enter the 2nd digit:')
c = input('Enter the 3rd digit:')

d = sorted([a, b, c])
print(f'Entered numbers: {d}')

print(f'{max(a, b, c)} is the largest number.')