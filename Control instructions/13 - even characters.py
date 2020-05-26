# Enter the text from the user.
# Display characters that are in even positions only.
# Perform usingsting -  slicing ( ‘abrakadabra’ -> ‘baaar’).

magic = input('Enter the spell: ')

magic = magic.replace(' ', '')

print(magic[1::2])