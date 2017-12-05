# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:25:47 2017

@author: xILENCE
"""
from math import *
import numpy as np


def show(self):
    for i in range(self.dimx):
        print(self.value[i])
    print(' ')

#def transpose(self):
#    #compute transpose
#    res = matrix([[]])
#    res.zero(self.dimy, self.dimx)
#    for i in range(self.dimx):
#        for j in range(self.dimy):
#            res.value[j][i] = self.value[i][j]
#    return res

def filter(x, P):
    for n in range(len(measurements)):
        
        #measurement update
        Z = np.matrix([[measurements[n]]]) 
        y = Z - (H * x)
        S = H * P * H.T + R
        K = P * H.T * S.I
        x = x + (K * y)
        
        P = (I - (K * H)) * P
        
        #prediction
        
        x = (x * F) + u
        P = F * P * F.T #F.transpose()
        
        print('x= ')
        show(x)
        print('P= ')       
        show(P)
    


measurements = [1, 2, 3]

x = np.matrix([[0.], [0.]]) #initial state (location and velocity)
P = np.matrix([[1000., 0.], [0., 1000.]]) #initial uncertainty
u = np.matrix([[0.], [0.]]) #external motion
F = np.matrix([[1., 1.], [0., 1.]]) #next state function
H = np.matrix([[1., 0]]) #measurement function
R = np.matrix([[1.]]) #measurement uncertainty
I = np.matrix([[1., 0.], [0., 1.]]) #identity matrix

filter(x, P)