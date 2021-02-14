# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 11:28:54 2021

@author: Matheus Cândido Carvalho - 5157
"""

#Implementação do Bubble Sort

entrada = [1,5,7,3,9,12,6,2,8]

length = len(entrada)

for i in range(length-1,0,-1):
        for j in range(i):
            if entrada[j] > entrada[j+1]:
                temp = entrada[j]
                entrada[j] = entrada[j+1]
                entrada[j+1] = temp
                
print(entrada)                




