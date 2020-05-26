# Ask 3 reviews for the script.
# Calculate average opinion.
# View Feedback: 7+ - very good | 5-7 average |  4- - not worth the attention.

print('Book rating: "Nightfall " Evelyn Duff.')
print('Enter your rating from 1 to 10:.')
opinionFirst = int(input('The main characters: '))
opinionSecond = int(input('Descriptions of nature: '))
opinionThird = int(input('Plot: '))

evaluation = (opinionFirst + opinionSecond + opinionThird) // 3

if evaluation <= 4:
    print('Feedback - not worth the attention.')

elif 5 >= evaluation <= 7:
    print('Feedback - average.')

else:
    print('Feedback - very good.')