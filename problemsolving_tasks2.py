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

# With an input list of integers, sort the elements starting with the largest positive integer, and ending with the smallest negative integer.

# For example, with the list [1, -3, 2, -5, 4, -1], the method should return [4, 2, 1, -1, -3, -5]

def sort_list(l: list) -> list:
  return []

# When method is ready, uncomment the following print command to test it

# print("-----------------------------\nTask 5: Sort list\n-----------------------------")
# print("Result: " + str(sort_list([1, -3, 2, -5, 4, -1])) + "\nExpected output: [4, 2, 1, -1, -3, -5]")
# print("Result: " + str(sort_list([1, 2, 3, 4, 5])) + "\nExpected output: [5, 4, 3, 2, 1]")


################################################
# Task 5.2
################################################

# The simple solution in a task like the one above is to use python's built-in sort method, which sorts the list in ascending order.

# If you used the sort method in the task above, try to implement the sorting algorithm yourself, without using the sort method. Instead
# you write the functionality yourself with if statements, loops, and variables.

# If you didn't use the sort method, try using this now instead and see how effective it is to use built-in methods for tasks.

def sort_list2(l: list) -> list:
  return []




################################################
# Task 6
################################################

# Safety and security is a huge concern when creating applications. We want to make sure that inputs from the users are valid and secure.
# When we as users use applications we often input our email address as a string.

# This string should meet some criteria to be valid: 

# Firstly, it should contain a '@' symbol. This symbol is used to separate the username from the domain name.
# The username should contain only letters, numbers, dots, and underscores.
# The domain name should contain only letters and one '.' symbol. Like "gmail.com" or "hotmail.com".

# Create one method that takes a string as input, and checks if the string is a valid email address. If the email is valid, return "VALID", otherwise return "INVALID".
# You can implement this using if statements and checks, or you could use regular expressions.
# See more about regular expressions/regex here: https://docs.python.org/3/library/re.html

# Using if statements, you might have to spilt up the input string using split() method, and then check each part of the email address separately.

def is_valid_email(email: str) -> str:
  return ""

# When method is ready, uncomment the following print commands to test it

# print("-----------------------------\nTask 6: Check if valid email\n-----------------------------")
# print("Result: " + is_valid_email("johan.hotmail.com") + "\nExpected output: INVALID")
# print("Result: " + is_valid_email("johan@") + "\nExpected output: INVALID")
# print("Result: " + is_valid_email("johan@hotmail") + "\nExpected output: INVALID")
# print("Result: " + is_valid_email("johan@hotmail.") + "\nExpected output: INVALID")
# print("Result: " + is_valid_email("@hotmail.com") + "\nExpected output: INVALID")
# print("Result: " + is_valid_email("johan@hotmailcom") + "\nExpected output: INVALID")
 
# print("Result: " + is_valid_email("johan@hotmail.com") + "\nExpected output: VALID")


################################################
# Task 6.2
################################################

# Passwords are another important part of security. When we create accounts on websites, we often have to create a password.
# The password should meet some criteria to be valid:

# The password should be at least 8 characters long.
# The password should contain at least one uppercase letter.
# The password should contain at least one lowercase letter.
# The password should contain at least one number.
# The password should contain at least one special character, like '@', '#', '$', '%', etc.

# Create one method that takes a string as input, and checks if the string is a valid password. If the password is valid, return "VALID", otherwise return "INVALID".

def is_valid_password(password: str) -> str:
  return ""

# When method is ready, uncomment the following print commands to test it

# print("-----------------------------\nTask 6.2: Check if valid password\n-----------------------------")
# print("Result: " + is_valid_password("Password") + "\nExpected output: INVALID")
# print("Result: " + is_valid_password("password") + "\nExpected output: INVALID")
# print("Result: " + is_valid_password("Password1") + "\nExpected output: INVALID")
# print("Result: " + is_valid_password("Password1@") + "\nExpected output: VALID")





