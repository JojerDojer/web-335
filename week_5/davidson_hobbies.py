#-------------------------------------------------------
#  Title: davidson_hobbies.py
#  Author: John Davidson
#  Date: 9 September 2023
#  Description: Exercise 5.3 for WEB 335 - Intro to NoSQL.
#-------------------------------------------------------

# A list of John's top five hobbies.
my_hobbies = ['gaming', 'watching movies', 'reading', 'lifting weights', 'hanging with friends']

# Using a for loop to iterate over the hobbies list and printing the results to console.
for hobby in my_hobbies:
    print (hobby)

# A list of each day of the week.
days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Loops through the list of each day of the week.
for day in days_of_week:
    # If the day in the list is Monday - Friday, print it is a work day.
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        print(f'Today is {day}, I have to work.')
    # Otherwise (if Saturday or Sunday), print it is a day off.
    else:
        print(f'Today is {day}, I have the day off and will enjoy my hobbies!')
