#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:20:17 2018

@author: sarthaksahu
"""

# =============================================================================
# 1. Write a Python program to create a tuple with different
# data types.
# =============================================================================

tuple1 = (1,2, (1,2,3), ("string1", "string2"))
print(tuple1)

print(type(tuple1))

# =============================================================================
# 2. Write a Python program to add an item in a tuple
# =============================================================================

tuple1 = tuple1 + (200, 300)
print(tuple1)

# =============================================================================
# Write a Python program to convert a tuple to a string
# =============================================================================

tuple2 = ('a','b','c','d', ("_stringsample",))
print(tuple2)

print(str(tuple2))
print("".join(map(str, tuple2)))

# =============================================================================
# 4. Write a Python program to get the 4th element and 4th
# element from last of a tuple.
# =============================================================================

tuple3 = (1,2,3,4,5,6,7,8,)
print(tuple3[3])
print(tuple3[-4])

# =============================================================================
# 5.Write a Python program to find the repeated items of a
# tuple
# =============================================================================

freq_count = {}
repeated_tuple = (1,1,1,3,4,3,4,5,3,3,5,6,7,8,9,10)
for i in repeated_tuple:
    if i in freq_count:
        freq_count[i]+=1
    else:
        freq_count[i] = 1

ans = []
for key in freq_count.keys():
    if freq_count[key] == 1:
        ans.append(key)

print(ans)


# =============================================================================
# 6. Write a Python program to check whether an element
# exists within a tuple
# =============================================================================

print(101 in repeated_tuple)

# =============================================================================
# 7. Write a Python program to convert a list to a tuple
# =============================================================================

print(ans)
ans = tuple(ans)
print(ans)
print(type(ans))

# =============================================================================
# 8. Write a Python program to slice a tuple
# =============================================================================

print(ans)
print(ans[2:4])

# =============================================================================
# 9. Write a Python program to find the length of a tuple
# =============================================================================

print(len(ans))

# =============================================================================
# 10. Write a Python program to convert a list of tuples into a
# dictionary
# =============================================================================

import random as r
sample_tuple = tuple(r.sample(range(1,100),5))
print(sample_tuple)
d = {}
for i in range(len(sample_tuple)):
    d[i] = sample_tuple[i]
print(d)













