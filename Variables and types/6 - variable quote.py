# Add a sentence to the quote variable:
quote = '„Honesty is the first chapter in the book of wisdom.”'
#„Honesty is the first chapter in the book of wisdom.”, next:

# Count the characters in the sentence
print(len(quote))
# Display the word "wisdom" from a sentence
print(quote[-8:-2])
# Displays only the first half of the sentence
middle = len(quote)//2
print(quote[0:middle])
# Display only dot
print(quote[-2])
# Display every third letter from the half of a sentence
print(quote[middle::3])
# Display ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])
# Display the sentence from the back
print(quote[::-1])
# Replace wisdom with friendship
print(quote.replace('wisdom', 'friendship'))