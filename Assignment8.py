# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:42:05 2020

@author: Sandhya
"""

import numpy as np
A= np.array([[9, 0 ,-6],[0, -4, 0],[-6, 0, 1]])
print("Given matrix: ")
print(A)
a = A[:,0]
b = A[:,1]
c = A[:,2]
#print(a, b, c)


r1 = np.linalg.norm(a)
q1 = a /r1
#print (r1, q1)

r2 = np.dot(q1,b)
r4 = np.linalg.norm(b - r2*q1)
#print (r2, r4)

q2 = (b - r2*q1)/r4
#print(q2)


r3 = np.dot(q1,c)
r5 = np.dot(q2,c)
r6 = np.linalg.norm(c - r3*q1 - r5*q2)
#print(r3,r5,r6)

q3 = (c - r3*q1 - r5*q2)/r6
#print(q3)


Q = np.zeros(A.shape)
Q[:, 0] = q1
Q[:, 1] = q2
Q[:, 2] = q3

R = np.array([[r1, r2, r3],[0, r4, r5],[0, 0, r6]])
print("Q = ")
print(Q)
print("R = ")
print(R)

A = Q@R
print("product of Q & R is")
print(A)