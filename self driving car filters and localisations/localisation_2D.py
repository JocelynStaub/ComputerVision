# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:45:58 2017

@author: xILENCE
"""


   
colors=[['red','green','green','red','red'],
        ['red','red','green','red','red'],
        ['red','red','green','green','red'],
        ['red','red','red','red','red']]
        
        
measurements = ['green','green','green','green','green']
motion = [[0, 0], [0, 1],[1, 0],[1, 0],[0, 1]]

sensor_correct = 0.7
p_move = 0.8

sensor_wrong = 1 - sensor_correct
p_stay = 1- p_move

def sense(p, colors, measurements):
    aux=[[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    s = 0.0
    for i in range(len(p)): #Actualise la distribution 
        for j in range(len(p[i])):
           hit = (measurements == colors[i][j]) 
           aux[i][j] = p[i][j] * (hit * sensor_correct + (1-hit) * sensor_wrong)
           s += aux[i][j] 
    for i in range(len(aux)):   #normalize
        for j in range(len(p[i])):
            aux[i][j] /= s
    return aux
    
def move(p, motion):
    aux=[[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    for i in range(len(p)):
        for j in range(len(p[i])):
            aux[i][j] = (p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])] + p_stay * p[i][j])
    return aux
    
def show(p):
    for i in range(len(p)):
        print(p[i])
    
pinit = 1.0 / float(len(colors)) / float(len(colors[0]))   #crée une distribution p uniforme en fonction du nb de colonnes et lignes
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]    #crée une distribution p uniforme en fonction du nb de colonnes et lignes

for k in range(len(measurements)):  #change la probabilité de distribution en fonction des capteurs et motions
    p = move(p,motion[k])
    p = sense(p, colors, measurements[k])
    
show(p)
