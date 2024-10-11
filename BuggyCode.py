# Exercise 1
# Task 1: Code Correction You are provided with a 
# Python script that uses conditional statements 
# to tell if a number is positive, negative, or zero, 
# but it has some errors. Identify and fix them.

# Original code
# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")


# My new code.
# Number needs to convert to integer to properly use these conditionals.
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
# number == 0 versus number =0. Looking to compare not redefine the variable.
elif number == 0:
    print("The number is zero.")
# Else did not need another condition since it should trigger when the first two conditions are not met.
else:
    print("The number is negative.")