# Exercise 2
# Task 1: Identify the Greatest 

# Write a Python program that asks the user to 
# enter three numbers. Your code should 
# then identify and print out the largest 
# number among the three.


# Set an empty list for the user information to be appended to.
numbers = []
# Setting a counter to use a while loop and make sure only 3 numbers are entered
counter = 3

# The while loop to have the user enter the data
while counter>0:
    user_input = int(input("This message will appear 3 times. Each time it appears please enter a number.\n"))
    numbers.append(user_input)
    counter -= 1
    print(f"You have {counter} left to enter.")

# Using the sorted function to sort the integers from smallest to largest.
sorted_nums = sorted(numbers)

# Printing out the sorted the largest and smallest numbers by indexing the last and first digits from the sorted list.
print(f"The largest number is {sorted_nums[-1]} and the smallest number is {sorted_nums[0]}.")
