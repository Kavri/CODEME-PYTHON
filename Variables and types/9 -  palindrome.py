#Is the sentence a palindome? Check.

print('******** PALINDROME ********')

palindrom_please = input('Enter the sentence: ')
palindrom_please = palindrom_please.lower()
palindrom_please = palindrom_please.replace(' ', '')

if palindrom_please is palindrom_please[::-1]:
    print('This sentence is a palindrome.')

else:
    print('This sentence is\'t a palindrome.')
