# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:10:47 2023

@author: koehc
"""

n,k=map(int,input().split())
scores=list(map(int,input().split()))
winner=0
k_score=scores[k-1]
for score in scores:
    if score>=k_score and score>0:
        winner+=1
print(winner)