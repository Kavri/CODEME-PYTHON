# Create a list.
# The list has dictionary values without duplicates.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

daysList = days.values()
daysList = list(daysList)


for k in daysList:
    daysList.remove(k)

print(daysList)