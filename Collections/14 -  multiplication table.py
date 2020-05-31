# Create a multiplication table as a nested list 10 x 10 list. Table has row x column multiplication results.

width = 50

print('-' * width)
for k in range(1,11):
    for m in range(1,11):
        print(f'{k * m:^4}', end='|')
    print()
    print('-' * width)