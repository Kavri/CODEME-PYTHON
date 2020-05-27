# The user enters 5 integers.
# Check if the first and last element is the same.

list = []

for number in range(5):
    number = int(input('Enter the number: '))
    list.append(number)

print(f'Entered numbers: {list}')

if list[0] == list[-1]:
    print('first and last element is the same')