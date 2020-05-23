# You create a script that will ask the user for - book title, author name, number of pages. Next:

title = input('Enter the title of the book: ')
surname = input('Enter author\'s name: ')
pages_num = input('Enter the number of pages: ')

#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
if title.isalpha() is True:
    print('The title has only letters.')
else:
    print('The title hasn\'t only letters.')

if surname.isalpha() is True:
    print('Surname has only letters.')
else:
    print('Surname has\'t only letters.')

if pages_num.isdigit() is True:
    print('Number of pages has only numbers.')
else:
    print('Number of pages has\'t only numbers.')
#Users are lazy sometimes. Sometimes they don't write the title and surname with a capital letter. Correct them :)
title_big = title.capitalize()
surname_big = surname.capitalize()
# Combine data into one book string using spaces:
book = [title_big, surname_big, pages_num]
print(' '.join(book))

#Policz liczbę wszystkich znaków w napisie book
a = 'book'
b = len(a)
print(f'The number of all characters in the {a} is {b}.')