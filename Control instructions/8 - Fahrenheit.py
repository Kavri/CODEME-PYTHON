#Celsjusz → Fahrenheit. The program is done in a loop from 0 to 200 Fahrenheit, every 20.

#C = 5/9 * (F - 32) # formula Celsius → Fahrenheit

#Write a solution using while / for.
print('.' * 84)

for c in range(0, 200, 20):
    cz = 5 / 9 * (c - 31)
    print(f'Temperature in degrees Fahrenheit: {c} | Temperature in degrees Celsius: {round(cz, 2)}')

fahr = 0

print('.' * 84)

while fahr <= 200:
    cel = C = 5/9 * (fahr - 32)
    print(f'Temperature in degrees Fahrenheit: {fahr} | Temperature in degrees Celsius: {round(cel, 2)}')
    fahr = fahr + 20