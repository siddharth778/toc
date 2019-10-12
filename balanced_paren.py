# -*- coding: utf-8 -*-
"""
Created on Sat Sept 12 12:22:25 2019

@author: SiddharthPorwal
"""

class Stack:
    def __init__(self):
        self.a=[]
    def push(self,i):
        self.a.append(i)
        print(self.a)
    def pop(self):
        self.a.pop()
    def size(self):    
        return len(self.a)
    def isempty(self):
        return len(self.a)==0
    def BalanceParenthesis(self):
        a = Stack()
        b = input("Enter string: ")
        print(self.a)
        for i in b:
            if (i=='('):
                self.push(i)
            elif(i==')'):
                self.pop()
        if (len(self.a)==0):
            print("YES")
        else:
            print("NO")           
s=Stack()
s.BalanceParenthesis()