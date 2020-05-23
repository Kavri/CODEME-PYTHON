#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = ('HokusPokus')
s2 = (' Tiger ')
print(f'Basic spell: {s1}')

a = len(s1)//2

partFirst = s1[:a]
partSecond = s1[a:]

magic = partFirst + s2 + partSecond
print(f'If you want to summon a tiger you say - {magic}!')