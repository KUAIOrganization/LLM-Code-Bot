#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:47:09 2023

@author: udayansharma
"""

n = int(input())
s = input()

# Number of changes reqd for first prefix of even length = 0 or 1 atmost.
# Num of changes reqd for second prefix = num changes (first prefix) + (0 or 1)
# So, we can use Dynamic Programming (Memoization):
    
# 1st prefix of even length of s = num_chnages[0] and so on..
num_changes = [0] * (n // 2)
s_out = s[0 : 2]
if s[0] == s[1]:
    num_changes[0] = 1
    if s[0] == "b":
        s_out = s_out.replace("b", "a", 1)
    else:
        s_out = s_out.replace("a", "b", 1)
    
for i in range(2, n - 1, 2):
    if s[i] == s[i + 1]:
        num_changes[i // 2] = num_changes[i // 2 - 1] + 1
        if s[i] == "b":
            s_out += "ab"
        else:
            s_out += "ba"
    else:
        num_changes[i // 2] = num_changes[i // 2 - 1]
        s_out += s[i : i + 2]
        
print(num_changes[-1])
print(s_out)