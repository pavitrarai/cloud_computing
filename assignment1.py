# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
# Question 1
# =============================================================================
print("\tTwinkle, Twinkle, little star, \nHow I wonder what you are!\n\tUp above the world so high,\n\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


# =============================================================================
# Question 2
# =============================================================================

import datetime

now = datetime.datetime.now()

print(now)
print(str(now))

# =============================================================================
# Question 3
#  Write a Python program which accepts the radius of a circle from the user and
#  compute the area.
# =============================================================================
import math as m
radius = int(input())
print(m.pi*radius**2)

# =============================================================================
# Question 4
# Write a Python program which accepts the user's first and last name and print
# them in reverse order with a space between them.
# =============================================================================

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(last_name+" "+first_name)

# =============================================================================
# Question 5
# Write a Python program to accept a filename from the user and print the
# extension of that. 
# =============================================================================

try:
    filename = input("Enter the filename: ")
    extension = filename.split('.')[1]
    print(extension)
except:
    print("No extension supplied !")

# =============================================================================
# Question 6
# Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.
# =============================================================================

n = int(input("Give an integer: "))
print(n + n**2 + n**3)

# =============================================================================
# Question 7
# Write a Python program to test whether a number is within 100 of 1000 or
# 2000.
# =============================================================================

n = int(input("Give an integer: "))
print(abs(1000-n) <= 100 or abs(2000-n) <= 100)

# =============================================================================
# Question 9
# Write a Python program to find whether a given number (accept from the
# user) is even or odd, print out an appropriate message to the user.
# =============================================================================

n = int(input("Give an integer: "))
if n%2 == 0:
    print("even")
else:
    print("odd")

# =============================================================================
# Question 10
# Write a Python program to count the number 4 in a given list.
# =============================================================================

number_list = [1,12,3,4,5,2,4,10,4,-4,0,4]
print(len([i for i in number_list if i==4]))

















