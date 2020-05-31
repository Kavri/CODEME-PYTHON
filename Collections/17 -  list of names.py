# Create a dictionary for 10 European countries.
# Each dictionary has a list of the 10 most popular female names.
# Add all lists.
# The new list has 100 elements.

dictUK = {}.fromkeys(['Meaghan', 'Dior', 'Adalee', 'Palmer', 'Oaklynn', 'Haisley', 'Keily', 'Novah', 'Yara', 'Ensley'], 'UK')
dictCanada = {}.fromkeys(['Abigail', 'Leah', 'Hazel', 'Violet', 'Aurora', 'Avery', 'Sofia', 'Camila', 'Aria', 'Scarlett'], 'Canada')
dictAustralia = {}.fromkeys(['Victoria', 'Madison', 'Luna', 'Grace', 'Leah', 'Hazel', 'Violet', 'Aurora', 'Zoey', 'Nora'], 'Australia')
dictNewZealand = {}.fromkeys(['Lily', 'Eleanor', 'Hannah', 'Lillian', 'Addison', 'Aubrey', 'Ellie', 'Stella', 'Natalie', 'Zoe'], 'New Zealand')
dictFrance = {}.fromkeys(['Leah', 'Hazel', 'Violet', 'Aurora', 'Savannah', 'Audrey', 'Brooklyn', 'Bella', 'Claire', 'Skylar'], 'France')
dictSpain = {}.fromkeys(['Lucy', 'Paisley', 'Everly', 'Anna', 'Caroline', 'Nova Genesis', 'Emilia', 'Kennedy', 'Samantha'], 'Spain')
dictIceland = {}.fromkeys(['Maya', 'Willow', 'Kinsley', 'Naomi', 'Aaliyah', 'Elena', 'Sarah', 'Ariana', 'Allison', 'Gabriella'], 'Iceland')
dictIsrael = {}.fromkeys(['Alice', 'Madelyn', 'Cora', 'Ruby', 'Eva', 'Serenity', 'Autumn', 'Adeline', 'Hailey', 'Gianna'], 'Israel')
dictMexico = {}.fromkeys(['Sofia', 'Isla', 'Eliana', 'Quinn', 'Nevaeh', 'Ivy', 'Sadie', 'Piper', 'Lydia', 'Alexa'], 'Mexico')
dictRussia = {}.fromkeys(['Svetlana', 'Emery', 'Julia', 'Olga', 'Arianna', 'Sofia', 'Irina', 'Tatiana', 'Brielle', 'Daria'], 'Russia')


listUK = list(dictUK)
listCanada = list(dictCanada)
listAustralia = list(dictAustralia)
listNewZealand = list(dictNewZealand)
listFrance = list(dictFrance)
listSpain = list(dictSpain)
listIceland = list(dictIceland)
listIsrael = list(dictIsrael)
listMexico = list(dictMexico)
listRussia = list(dictRussia)

lista = listUK + listCanada + listAustralia + listNewZealand + listFrance + listSpain + listIceland + listIsrael + listMexico + listRussia

# Display names that are in a minimum of 3 countries.

list = []
for name in lista:
    coun = lista.count(name)
    if coun >= 3:
        list.append(name)

for m in list:
    list.remove(m)

print(list)