# The user enters 10 numbers.
# Numbers displayed - odd numbers

list = []

for number in range(10):
    number = int(input('Proszę o podanie cyfry:'))
    number = round(number)
    if number % 2 != 0:
        list.append(number)

print(f'Odd numbers: {list}.')