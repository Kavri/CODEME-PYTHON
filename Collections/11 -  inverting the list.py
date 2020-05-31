# Split the list into three parts
# Reverse each list

#input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#output:
#[4, 3, 2, 1]
#[14, 13, 12, 11]
#[24, 23, 22, 21]

list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

list1 = list[:4]
list2 = list[4:8]
list3 = list[8:]

list1.reverse()
list2.reverse()
list3.reverse()

print(list1)
print(list2)
print(list3)