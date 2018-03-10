#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:52:48 2018

@author: sarthaksahu
"""

# =============================================================================
# 1. Write a Python program to sum all the items in a list
# =============================================================================
import random as r

sample_list = list(range(0,10,2))
r.shuffle(sample_list)
print(sample_list)
print(sum(sample_list))

# =============================================================================
# 2. Write a Python program to get the largest number from a list.
# =============================================================================

print(max(sample_list))

# =============================================================================
# 3. Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples
# =============================================================================

def sort_helper(x):
    return x[1]

sample_list = [(1,2),(0,-1),(2,0), (4,4), (-5,10)]
print(sample_list)
sample_list.sort(key=sort_helper)
print(sample_list)

# Another way :- sample_list.sort(key=lambda x:x[1])

# =============================================================================
# 4. Write a Python program to remove duplicates from a list
# =============================================================================

sample_list = [1,1,1,2,3,3,4,5,6,7,7,7,8,9]
r.shuffle(sample_list)
print(sample_list)
sample_list = list(set(sample_list))
print(sample_list)

# =============================================================================
# 5. Write a Python program to find the list of words that are longer
# than n from a given list of words
# =============================================================================

words_list = ["Sarthak", "Mountains", "Sea", "Trains", "Rainbow", "Flowers", "Kids"]
print([i for i in words_list if(len(i) > 5)])


# =============================================================================
# 6. Write a Python program to get the difference between the two lists
# =============================================================================

list1 = r.sample(range(0,100),5)
list2 = r.sample(range(0,100),5)
print("list1: {}".format(list1))
print("list2: {}".format(list2))
print([i-j for i,j in zip(list1,list2)])

# =============================================================================
# 7. Write a Python script to add a key to a dictionary
# =============================================================================

d = {}
print(d)
d[1] = 5
print(d)

# =============================================================================
# 8. Write a Python script to concatenate following dictionaries to
# create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# =============================================================================

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {}
for d in [dic1, dic2, dic3]:
    dic4.update(d)
print(dic4)

# =============================================================================
# 9. Write a Python program to remove a key from a dictionary
# =============================================================================

print(dic4)
dic4.pop(6)
print(dic4)


# =============================================================================
# 10.Write a Python program to multiply all the items in a dictionary
# =============================================================================
k = 1
for i in list(dic4.values()):
    k = k*i
print(k)


















