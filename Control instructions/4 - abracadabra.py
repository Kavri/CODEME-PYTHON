#Create a variable that has a string.
#Check if the string: is longer than 5 characters | has the letter a.
#If the string has a - wreplace all letters a with z | display string.

magic = 'Abracadabra'

print('Check if the string: is longer than 5 characters | has the letter a.')
magicNumb = len(magic)
if magicNumb > 5:
    print('String is longer than 5 characters.')
else:
    print('String is less than 5 characters.')

magic = magic.lower()
print('Occurrence of the character "a":' , end = ' ')
print(magic.count('a'),'.')
t = magic.count('a')

print()
print('If the string has a - wreplace all letters a with z | display string.')

if t > 0:
    print(magic.replace('a', 'z'))
else:
    print('String has\'t "a".')