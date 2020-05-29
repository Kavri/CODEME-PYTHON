# Create 2 tuples.
# Then create a list - combination of elements with an even index of 1 tupla,
# and odd elements from a second tupla. Display in list - set.

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple2 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

result = list(tuple1[::2] + tuple2[1::2])
result = set(result)

print(result)