# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4

import math
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        #print("done!")
        break
    try:
        value = float(num)
    except:
        print("invalid input")
        continue
    if largest == None:
        largest = -1 * math.inf
    if smallest == None:
        smallest = math.inf
    if value < smallest:
        smallest = value
        continue
    elif value > largest:
        largest = value
    
print("Maximum", largest)
print("minimum", smallest)