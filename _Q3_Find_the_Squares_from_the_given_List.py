#Write a Python program to square the elements of a list using map() function.


size= int(input("enter the size of list: \n"))            # taking the number od elements to be entered in list
lst = []
for i in range(size):
    elements=int(input("Enter list elements:"))         # entering the elements
    lst.append(elements)                                # appending all the eneterd elements in a list
print("\nOriginal list: ",lst)                            # printing original list

result = map(lambda x: x * x, lst)                       # using map function
print("\nSquare of given list elements:", list(result))
