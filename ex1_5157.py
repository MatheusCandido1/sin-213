# -*- coding: utf-8 -*-
"""
Created on Sun Feb 6 11:34:54 2021

@author: Matheus Cândido Carvalho - 5157
"""

#Implementação de soma de Triplas


entrada = [30, -30, -20, -10, 40, 0, 10, 5]

length = len(entrada)

cont = 0

for i in range(0,length-2):
    for j in range(i+1, length-1):
        for k in range(j + 1, length):
            if(entrada[i]+entrada[j]+entrada[k] == 0):
                cont += 1
    
    
print('A entrada possui ' + str(cont) + ' triplas')
