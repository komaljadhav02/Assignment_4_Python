# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

number= lambda x : x + 25        # using variable number to store the function object

n = int(input("Enter the number :- "))   # using input function to take input from user

print(number(n))      # calling lambda function by passing an argument