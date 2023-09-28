# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:18:34 2023

@author: Zinc
"""

n=int(input())
s=[int(y) for y in input().split()]
list=[]
for i in range(1,n+1):
    list.append(s.index(i)+1)
print(' '.join(str(x) for x in list))