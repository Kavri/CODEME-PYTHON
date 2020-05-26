# The user enters the names (
# Następnie powitaj każdą osobę na liście.

print('First template - Welcome:')
list = []
name = input('Enter names separated by a space: ')

list.append(name)

print('People on the list:', list, 'Welcome!')

print(' ')
print('Second template - Welcome:')

names = input('Enter names separated by a space: ')

names = names.split(' ')
print('People on the list:', names)


welcome = (' nice to meet you!')

for person in names:
    print(person + welcome)