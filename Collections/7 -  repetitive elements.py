# Create a tuple.
# Find duplicate items.

tuple = (1, 2, 3, 4, 2, 3, 1, 12)

a = tuple.count(1)
b = tuple.count(2)
c = tuple.count(3)
d = tuple.count(4)
e = tuple.count(12)

tuple2 = list(tuple)
repeatingList = []

if a > 1:
    repeatingList.append(tuple2[0])
elif b > 1:
    repeatingList.append(tuple2[1])
elif c > 1:
    repeatingList.append(tuple2[2])
elif d > 1:
    repeatingList.append(tuple2[3])
elif e > 1:
    repeatingList.append(tuple2[8])
else:
    print('No repetitive elements.')

print(f'Repetitive elements: {repeatingList}')