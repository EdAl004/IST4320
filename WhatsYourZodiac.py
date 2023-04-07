# Name: Edgar Alatorre, Sergio Beckner
# WhatsYourZodiac V1
# Date: 11/27/2022

# This program will take in the user's birthdate information and return their zodiac classification based on either the Chinese zodiac scheme or Astrological zodiac scheme.

# Create a banner to entice the user
print('********************************************************************************')
print('Welcome! Ready to learn what your sign is? Please follow the instructions below!')
print('********************************************************************************\n')


# Ask for user's birthdate information
month = int(input('Please enter the month of your birth (e.g. 01, 12 etc): '))
day = int(input('Please enter your day of your birth (e.g. 15, 31 etc): '))
year = int(input('Please enter the year of your birth (e.g. 1990, 2002 etc): '))


# Take the birthdate information from a file-input and store the values in their appropriate variables (Month, Day, Year)
#doc = input("Please enter file path: ")

# with open(doc, 'r') as file:
#    data = file.readlines()
#    for line in data:
#        month = line[0:2]
#        month = int(line[0:2])

#print('Your month is: ', month)

# with open(doc, 'r') as file:
#    data = file.readlines()
#    for line in data:
#       day = line[3:5]
#        day = int(line[3:5])

#print('Your day is: ', day)

# with open(doc, 'r') as file:
#    data = file.readlines()
#    for line in data:
#        year = line[5:9]
#        year = int(line[6:10])

#print('Your year is: ', year)


# Create the algorithm that will assign the correct Astrological zodiac classification based on month and day.
# Output the result.
if month == 12:
    if day < 22:
        astro = 'Sagittarius'
    else:
        astro = 'Capricorn'
elif month == 1:
    if day < 20:
        astro = 'Capricorn'
    else:
        astro = 'Aquarius'
elif month == 2:
    if day < 19:
        astro = 'Aquarius'
    else:
        astro = 'Pisces'
elif month == 3:
    if day < 21:
        astro = 'Pisces'
    else:
        astro = 'Aries'
elif month == 4:
    if day < 20:
        astro = 'Aries'
    else:
        astro = 'Taurus'
elif month == 5:
    if day < 21:
        astro = 'Taurus'
    else:
        astro = 'Gemini'
elif month == 6:
    if day < 21:
        astro = 'Gemini'
    else:
        astro = 'Cancer'
elif month == 7:
    if day < 23:
        astro = 'Cancer'
    else:
        astro = 'Leo'
elif month == 8:
    if day < 23:
        astro = 'Leo'
    else:
        astro = 'Virgo'
elif month == 9:
    if day < 23:
        astro = 'Virgo'
    else:
        astro = 'Libra'
elif month == 10:
    if day < 23:
        astro = 'Libra'
    else:
        astro = 'Scorpio'
elif month == 11:
    if day < 22:
        astro = 'Scorpio'
    else:
        astro = 'Sagittarius'

print("\nYour Astrological sign is:\n", astro)

pause = input("\nPress enter if your ready for your Eastern zodiac\n")


# Create the algorithm that will assign the correct Chinese zodiac classification based on the year.
# Output the result.
def east(year):
    if (year - 2000) % 12 == 0:
        print('Your Chinese Zodiac sign:\n Dragon')
    elif (year - 2000) % 12 == 1:
        print('\nYour Chinese Zodiac sign:\n Snake')
    elif (year - 2000) % 12 == 2:
        print('Your Chinese Zodiac sign:\n Horse')
    elif (year - 2000) % 12 == 3:
        print('Your Chinese Zodiac sign:\n sheep')
    elif (year - 2000) % 12 == 4:
        print('Your Chinese Zodiac sign:\n Monkey')
    elif (year - 2000) % 12 == 5:
        print('Your Chinese Zodiac sign:\n Rooster')
    elif (year - 2000) % 12 == 6:
        print('Your Chinese Zodiac sign:\n Dog')
    elif (year - 2000) % 12 == 7:
        print('Your Chinese Zodiac sign:\n Pig')
    elif (year - 2000) % 12 == 8:
        print('Your Chinese Zodiac sign:\n Rat')
    elif (year - 2000) % 12 == 9:
        print('Your Chinese Zodiac sign:\n Ox')
    elif (year - 2000) % 12 == 10:
        print('Your Chinese Zodiac sign:\n Tiger')
    else:
        print('Your Chinese Zodiac sign:\n Rabbit')


east(year)

pause = input("\nPress enter when you are done reading the results.")
