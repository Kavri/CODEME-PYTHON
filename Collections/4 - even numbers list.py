# The user enters numbers into the list.
# Check if the middle 2 digits are the same.

list = []


for number in range(6):
    number = int(input('Enter the number:'))
    list.append(number)

print(f'Entered digits: {list}')
if list[2] == list[-3]:
    print('The middle 2 elements are the same.')