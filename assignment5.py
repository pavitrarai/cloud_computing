#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:21:30 2018

@author: sarthaksahu
"""
# =============================================================================
# 1. Create a text file named “INPUT” that comprises of some text. Using Mapper and Reducer
# program generate a KEY and COUNT matrix for the file.
# =============================================================================
from functools import reduce
word_list = []
with open("input.txt") as f:
    word_list = [word for line in f for word in line.split()]
    
count_mappings = list(map(lambda x: (x,1), word_list))
#print(count_mappings)

def reducer(word, count, word_dict):
    if word in word_dict:
        word_dict[word] += count
    else:
        word_dict[word] = count

word_dict = {}
word_count = list(reduce(reducer, count_mappings))
