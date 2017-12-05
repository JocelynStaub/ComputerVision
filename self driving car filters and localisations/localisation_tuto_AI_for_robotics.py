# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 14:17:01 2017

@author: xILENCE
"""

p=[0.2,0.2,0.2,0.2,0.2]
world=['green','red','red','green','green']
measurements = ['red','red']
motion = [1, 1]
pHit=0.6
pMiss=0.2
pExact = 0.8
pUndershoot = 0.1
pOvershoot = 0.1


def sense(p,Z):
    q=[]
    for i in range(len(p)):
        if Z == world[i]:
            q.append(p[i] * pHit)
        else:
            q.append(p[i] * pMiss)
    s = sum(q)
    for i in range(len(p)):
        q[i] = q[i] / s
    return q
    
def move(p, U):
    q=[]
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pUndershoot * p[(i-U-1) % len(p)]
        s = s + pOvershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
    
    

for k in range(len(measurements)):
    p = sense(p,measurements[k])
    p = move(p, motion[k])
    
print p