# Write currency converter.
# The program will ask the user for the amount of money
# then the program will convert the amount into euros or dollars
# Ignore the cents


print('ONLINE EXCHANGE OFFER - LOW PRICES')

exchangeEuro = 4.19
exchangeDolar = 3.90

moneyHoliday = float(input('Enter the amount of money: '))
print(f'The amount entered - {moneyHoliday}.')



currencyWhat = input('What currency will you use? Enter EURO or DOLLAR: ')
if currencyWhat == 'DOLLAR':
    calculationEuro = moneyHoliday / exchangeDolar
    print(f'The amount is {round(calculationEuro)} €')
else:
    calculationDollar = moneyHoliday / exchangeDolar
    print(f'The amount is {round(calculationDollar)} $')


print('Have a nice trip!')