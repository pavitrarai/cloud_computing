#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:27:38 2018

@author: sarthaksahu
"""

# =============================================================================
# 1. Write a Python program to test whether a passed letter is a vowel
# or not.
# =============================================================================

letter = input("input an alphabet: ")
vowels = ['a','e','i', 'o', 'u']
print(letter.lower() in vowels)

# =============================================================================
# 2. Write a Python program to print out a set containing all the colors
# from color_list_1 which are not present in color_list_2.
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# =============================================================================

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)

# =============================================================================
# 3. Write a Python program to solve (x + y) * (x + y).
# =============================================================================

x = int(input())
y = int(input())
print((x+y)**2)

# =============================================================================
# 4. Write a Python program to calculate the sum of the digits in an
# integer.
# =============================================================================

n = 123456
print(sum([int(i) for i in str(n)]))

# =============================================================================
# 5. Write a Python program to calculate the length of a string.
# =============================================================================

sample_string = input("input a string: ")
print(len(sample_string))

# =============================================================================
# 6. Write a Python program to get a single string from two given
# strings, separated by a space and swap the first two characters of
# each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
# =============================================================================

str1 = 'abc'
str2 = 'xyz'

str1,str2 = str2,str1
print(str1 + " " + str2)

# =============================================================================
# 7. Write a Python program to remove the nth index character from a
# nonempty string.
# =============================================================================

sample_string = "Sarthak- Sahu"
sample_string = sample_string[:7] + sample_string[8:]
print(sample_string)

# =============================================================================
# 8. Write a Python script that takes input from the user and displays
# that input back in upper and lower cases.
# =============================================================================

sample_string = input("input a string: ")
print(sample_string.upper())
print(sample_string.lower())

# =============================================================================
# 9. Write a Python function to insert a string in the middle of a string.
# =============================================================================

sample_string = "blahblah"
mid = len(sample_string)//2
mid_string = "boom"
sample_string = sample_string[:mid] + mid_string + sample_string[mid:]  
print(sample_string)

# =============================================================================
# 10.Write a Python program to print the floating numbers upto 2
# decimal places with a sign.
# =============================================================================
import math as m
floating_num = m.pi
print("{:.2f}".format(floating_num))





































