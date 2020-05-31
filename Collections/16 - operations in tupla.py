# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

exampleList = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

exampleList = exampleList.copy()
exampleList = tuple(exampleList)

a = min(exampleList)
b = max(exampleList)

print(f'Minimal number: {a}')
print(f'Maximum number: {b}')