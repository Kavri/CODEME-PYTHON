#Create a two-dimensional array
#the rows contain people details
#in the columns are - name | surname | profession
#Dorota, Wellman, journalist
#Adam, Małysz, athlete
#Robert, Lewandowski, footballer
#Krystyna, Janda, actress

list = [
    ['Dorota', 'Wellman', 'journalist'],
    ['Adam', 'Małysz', 'athlete'],
    ['Robert', 'Lewandowski', 'footballer'],
    ['Krystyna', 'Janda', 'actress']
]

width = 65
print('-' * width)
print(f'|NAME: {list[0][0]}  |', f'|SURNAME: {list[0][1]}    |', f'|PROFESSION : {list[0][2]}|')
print(f'|NAME: {list[1][0]}    |', f'|SURNAME: {list[1][1]}     |', f'|PROFESSION : {list[1][2]}   |')
print(f'|NAME: {list[2][0]}  |', f'|SURNAME: {list[2][1]}|', f'|PROFESSION : {list[2][2]}|')
print(f'|NAME: {list[3][0]}|', f'|SURNAME: {list[3][1]}      |', f'|PROFESSION : {list[3][2]}   |')
print('-' * width)