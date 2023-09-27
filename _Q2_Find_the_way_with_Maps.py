#Write a Python program to triple all numbers of a given list of integers. Use Python map.

size= int(input("enter the size of list: \n"))   # the number od elements to be entered in list
lst = []
for i in range(size):
    elements=int(input("Enter list elements: "))  # entering the elements
    lst.append(elements)                         # appending all the eneterd elements in a list
print("\nOriginal list: ",lst)                     # printing original list

 

result = map(lambda x: x * 3, lst)               # using map function
print("\nTriple of given list elements:", list(result))
                    