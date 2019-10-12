# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:05:08 2019

@author: SiddharthPorwal
"""
n=input()
count0=0
count1=0
for i in n:
    if i=='0':
        count0=count0+1
for x in n:
    if x=='1':
        count1=count1+1
if(count0==count1):
    print("There are equal no of 0's and 1's.")
else:
    print("There are unequal no of 0's and 1's.")