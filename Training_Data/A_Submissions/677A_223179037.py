# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:30:50 2023

@author: gzk16
"""

n, h = map(int, input().split())
height = list(map(int, input().split()))
count = 0
for high in height:
    if high <= h:
        count = count + 1
    else:
        count = count + 2
print(count)