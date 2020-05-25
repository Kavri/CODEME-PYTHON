numb = float(input('Enter the number: '))

numb = numb % 3

if numb == 0:
    print(f'{numb} is divisible by 3.')
else:
    print(f'{numb} isn\'t divisible by 3.')