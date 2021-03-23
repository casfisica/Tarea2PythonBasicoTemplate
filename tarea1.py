# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:01:54 2021

@author: david
"""

import funciones as fun #Importa las funciones creadas

def one_sided_prob(n,k): #Calcula la probabilidad de obtener k caras o sellos al realizar n lanzamientos de moneda
    return fun.Binomial(n,k)/(2**n) #calcula la probabilidad entre 0 y 1

p1 = one_sided_prob(100, 10)#Calcula la probabilidad de obtener diez caras o sellos al realizar cien lanzamientos

print("\n La probabilidad de obtener diez caras en cien lanzamientos es " + str(p1))

p2 = 0 #Variable sobre la cual realizar las suma de probabilidad
k = 31 #Numero de caras a partir se satisface la condición y se inicia la suma de probabilidad
while (k <= 100): #Itera sobre todos los casos en que se cumpla que hay más de 30 caras
    p2 = p2 + one_sided_prob(100, k) #Calcula la probabilidad de tener k caras y la suma a la probabilidad total
    k = k + 1 #Aumenta el numero de caras para el estudio de probabiliad
    
print("\n La probabilidad de obtener más de 30 caras en cien lanzamientos es " + str(p2))
