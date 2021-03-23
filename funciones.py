# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:45:44 2021

@author: david
"""

def Factorial(n): #Retorna el factorial de un numero entero no negativo
    if (type(n) != int): #Verifica que el argumento sea entero
        print("Solo se admiten enteros")
        return
    i = 1 #variable para contar factores en la productoria
    r = 1 #Variable para almacenar la productoria
    while (i <= n): #Itera entre factores de la productoria
        r = r*i #Multiplica el nuevo factor junto con los anteriores
        i = i+1 #Pasa al siguiente factor en la productoria
    return int(r)

def Binomial(n,k):
    if (type(n) != int): #Verifica que el argumento sea entero
        print("Solo se admiten enteros")
        return
    return int( Factorial(n)/( Factorial(k) * Factorial(n-k) ) ) #Calcula el coeficiente binomial usando la función Factorial

def Pascal(n):
    if (type(n) != int): #Verifica que el argumento sea entero
        print("Solo se admiten enteros")
        return
    i = 0 #Contador para la linea del triangulo de Pascal
    while (i <= n): #Itera sobre las filas del triangulo
        k = 0 #contador para los coeficientes de la fila actual
        print("n=" + str(i) + "~"*(n-i+1),end = '')
        while (k < i+1):#itera sobre cada coeficiente de la fila actual
            print(str(Binomial(i,k))+" ",end='') #Imprime el coeficiente actual más un espacio
            k = k + 1 #Pasa al siguiente coeficiente
        print("\n") #Realiza un salto de linea
        i = i + 1 #Pasa a la siguiente fila
    return
    
