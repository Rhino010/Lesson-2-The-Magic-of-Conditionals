# Exercise: 3

# Task 1: Leap Year Checker Write a Python program 
# that prompts the user to input a year. The program 
# should determine if the given year is a leap year
#  or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, but these 
# centurial years are leap years if they are exactly divisible by 400.

# Declaring the variable year and converting it to integer for comparison
year = int(input("Please enter the year you would like to check."))

# Setting all conditionals based on most pertinent absolutes for determining what is and is not a leap year.
if year%400 == 0:
    print(f"The year {year} is a leap year.")
elif year%100 == 0:
    print(f"The year {year} is not a leap year.")
elif year%4 == 0:
    print(f"The year {year} is a leap year.")
else:
    print("Nope it does not meet the criteria of a leap year.")