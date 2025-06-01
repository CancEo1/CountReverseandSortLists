# Purpose: Count, reverse, and sort lists of numbers
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
count = numlist.count(14) # Count occurrences of 14 @@This is how you accomplish project 1 find the occurences of the word and count them@@
numlist.reverse() # Reverse the list
numlist.sort() # @@I think this is for Project 2 sort the list and to find it with the first letter@@
print("Count of 14:", count) # Print the count of 14

# How to use the sort() method with mixed-case lists
# Capital letters will come before lower case by default
foodlist = ["apple", "Banana", "cherry", "date", "Elderberry"]
foodlist.sort()
count = foodlist.count("Banana") # Count occurrences of "Banana" for practice for project 1. VERY IMPORTANT FUNCTION of Python and Project 1
print(foodlist) # Print the sorted food list
print("Count of 'Banana':", count) # Print the count of "Banana"

# Using key arguments to fix the sort order
foodlist.sort(key=str.lower) # Sort the food list ignoring case
print(foodlist) # Print the food list sorted ignoring case

print("What happens in a simple sort with mixed-case lists:")
# This will show how mixed-case sorting works by default
foodlist = ["apple", "Banana", "cherry", "date", "Elderberry"]
sorted_foodlist = sorted(foodlist) # Sort the food list using sorted() function
print(sorted_foodlist)

# Using the min and max functions as well as the sum() choice and shuggle functions
print("Using min, max, and sum functions:")
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]

minimum = min(numlist) # Find the minimum value in the list
maximum = max(numlist) # Find the max value in the list
total = sum(numlist) # Calculate the sum of the list
print("Results", minimum, maximum, total) # Print the results

# Using the choice() and shuffle functions from the random module
import random
choice = random.choice(numlist) # Randomly select an element from the list
random.shuffle(numlist) # Shuffle the list randomly
print("Results: ", choice, numlist) # Print for tests

# Deep copy of a list for independent manipulation
print("Deep copy of a list:")
import copy
list_one = [1, 2, 3, 4, 5]
list_two = copy.deepcopy(list_one) # Create a deep copy of list_one
list_two[1] = 4
print(list_one) # Print original list
print(list_two) # Print modified copy

# Slicing a list
# Syntax for slicing mylist[start:end:step]

# Code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[0:2] # Get the first two elements
numbers[:2] # Same as above, get the first two elements
numbers[4:] # Get all elements from index 4 to the end

# Slicing with a step
numbers[0:4:2] # Get every second element from the first four elements
numbers[::-1] # Reverse the list using slicing

# Cancatenate two lists with the + and += operator
inventory = ["sword", "shield", "potion"]
print("Opened chest")
chest = ["gold", "scroll"]
combined = inventory + chest # combine two lists
print(inventory)
inventory += chest
print(inventory)