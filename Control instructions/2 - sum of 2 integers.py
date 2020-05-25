#Get 2 integers. .Calculate the sum
# If the sum is greater than 100 - display the result.
# If the sum is less than 100 - display "End!".

numb_1 = int(input('Enter the first integer: '))
numb_2 = int(input('Enter the second integer: '))

amount = numb_1 + numb_2

if amount > 100:
    print(f'The sum of integers: {amount}')
else:
    print('End!')