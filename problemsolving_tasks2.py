################################################
# Preparation
################################################

# You need python installed
# You can download it from https://www.python.org/downloads/

# Test this code by executing it in a command line or terminal
# You do this by navigating to the folder where this file is located in the terminal
# Here, you run the program by typing "py problemsolving_tasks2.py" and pressing enter




################################################
# Task 1
################################################

# Recursion is when a method calls itself. For example a method counting down from an integer n to 0 could look like this:

# def countdown(n: int):
#      if n == 0:
#        return print(n)
#      else:
#        print(n)
#        return countdown(n - 1)  
     
# The recursion happens on line 6, where the method calls itself with the argument n - 1.
# For example, for countdown(3) this is what happens:

# countdown(3) 
# --> print(3) + countdown(2)
#                --> print(2) + countdown(1)
#                               --> print(1) + countdown(0)
#                                              --> print(0)

# The crucial part using recursion is to have a base case that stops the recursion, like line 2 in the example above. When n == 0
# the recursion ends, and the method stops executing. If the base case is missing, the method will keep calling itself, continuing
# onto negative numbers until the program crashes, or you cancel the execution.


# Using recursion, write the following method taking positive integer n as input, and calculating the sum of all positive integers from 1 to n:

def pos_integer_sum(i: int) -> int:
  return 0

# When method is ready, uncomment the following print command to test it

# print("-----------------------------\nTask 1: Positive integer sum with recursion\n-----------------------------")
# print("Result: " + str(pos_integer_sum(5)) + "\nExpected output: 15")
# print("Result: " + str(pos_integer_sum(0)) + "\nExpected output: 0")


################################################
# Task 1.2
################################################

# The method you implemented above might have a vulnerability. Can you think of a type of input that would cause the method run indefinitely?

# If you haven't already, add an additional if statement to the method above to check for this type of input, and return 0 if it occurs.




################################################
# Task 2
################################################

# Write a method that takes a list of integers as input, and returns a new list containing only the even numbers from the input list.

def only_even_numbers(numbers: list) -> list:
  return []

# When method is ready, uncomment the following print command to test it

# print("-----------------------------\nTask 2: Only even numbers\n-----------------------------")
# print("Result: " + str(only_even_numbers([1, 2, 3, 4, 5, 6])) + "\nExpected output: [2, 4, 6]")
# print("Result: " + str(only_even_numbers([1, 3, 5])) + "\nExpected output: []")
# print("Result: " + str(only_even_numbers([2, 4, 6])) + "\nExpected output: [2, 4, 6]")


################################################
# Task 2.2
################################################

# Using the method you implemented above, write a new method that takes a list of integers as input, and returns a new list containing only the odd numbers from the input list.

def only_odd_numbers(numbers: list) -> list:
  return []

# When method is ready, uncomment the following print command to test it

# print("-----------------------------\nTask 2.2: Only odd numbers\n-----------------------------")
# print("Result: " + str(only_odd_numbers([1, 2, 3, 4, 5, 6])) + "\nExpected output: [1, 3, 5]")
# print("Result: " + str(only_odd_numbers([2, 4, 6])) + "\nExpected output: []")




################################################
# Task 3
################################################

# With input list, reverse the order of the elements in the list, and return the reversed list

def reverse_list(l: list) -> list:
  return []

# When method is ready, uncomment the following print command to test it

# print("-----------------------------\nTask 3: Reverse list\n-----------------------------")
# print("Result: " + str(reverse_list([1, 2, 3, 4, 5])) + "\nExpected output: [5, 4, 3, 2, 1]")




################################################
# Task 4
################################################

# With input integer n and list, write a method that checks if n is in the list. If n is in the list, return "FOUND", otherwise return "NOT FOUND"

def check_if_in_list(n: int, l: list) -> str:
  return ""

# When method is ready, uncomment the following print commands to test it

# print("-----------------------------\nTask 4: Check if in list\n-----------------------------")
# print("Result: " + check_if_in_list(5, [1, 2, 3, 4, 5]) + "\nExpected output: FOUND")
# print("Result: " + check_if_in_list(6, [1, 2, 3, 4, 5]) + "\nExpected output: NOT FOUND")


################################################
# Task 4.2
################################################

# Using the method above, write a method returning the index of the element n in the list. If n is not in the list, return -1

# Index is the position of an element in a list. The first element in a list has index 0, the second element has index 1, and so on.

def find_index_of_element(n: int, l: list) -> int:
  return -1

# When method is ready, uncomment the following print commands to test it

# print("-----------------------------\nTask 4.2: Find index of element\n-----------------------------")
# print("Result: " + str(find_index_of_element(5, [1, 2, 3, 4, 5])) + "\nExpected output: 3")
# print("Result: " + str(find_index_of_element(6, [1, 2, 3, 4, 5])) + "\nExpected output: -1")


################################################
# Task 4.3
################################################

# What will happen if you try to find the index of an element that is in the list multiple times?

# For example, what will happen if you try to find the index of 5 in the list [1, 2, 3, 4, 5, 5, 6]?

# If the method above does not handle this case, modify it to return the index of the first occurrence of n in the list,
# or all occurrences of n in the list as a list of indices.




################################################
# Task 5
################################################



