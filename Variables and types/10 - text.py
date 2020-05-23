letters = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

separation = '.' * 69

print(separation)
print('✓ Count the number of "better" in the text.')
print(letters.count('better'))
print('')

print(separation)
print('✓ Remove the star from text.')
letters = letters.replace('*', '')
print(letters)

print(separation)
print('✓ Replace one instance of "explain" with "understand".')
letters = letters.replace('explain', 'understand')
print(letters)

print(separation)
print('✓ Delete spaces and all words "-" combined.')
letters = letters.replace(' ', '-')
print(letters)

print(separation)