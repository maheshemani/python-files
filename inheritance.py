# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:56:55 2020

@author: mahesh.emani
"""

class A:
    def testa(self):
        print("in A")
        
class B(A):
    def testb(self):
        print("in B")

b=B()
b.testa()
b.testb()

class C(B):
    def testc(self):
        print("in C")

c=C()
c.testa()
c.testb()
c.testc()


