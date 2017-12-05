# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:45:52 2017

@author: xILENCE
"""

from math import *

def f(mu, sigma2, x):
    qex = exp((-1./2.) * pow((x-mu),2)/sigma2)
    c = 1./sqrt(2.*pi*sigma2)
    q = c * qex
    return q
    
    
    
def newgauss(mu, nu, sigma2, r2):
    mupost = 1./(sigma2+r2)*(r2*mu+sigma2*nu)
    sigma2post = 1./((1./sigma2)+(1./r2))    

    return [mupost, sigma2post]
    
#print f(10., 4., 8.)
print newgauss(10.,13.,8.,2.)