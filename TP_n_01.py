# 5 - Desarrollar una función que permita convertir un número romano en un número decimal.

n_romanos = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

def convertir_romano_a_decimal (num, pos, n_romanos):
    if (pos==(len(num)-1)):
        return n_romanos[num[pos]]
    else:
        romana_actual = n_romanos [num[pos]]
        ronana_siguiente = n_romanos [num[pos + 1]]
        if (romana_actual < ronana_siguiente):
            return - romana_actual + convertir_romano_a_decimal (num, pos + 1, n_romanos)
        else:
            if (romana_actual >= ronana_siguiente):
                return romana_actual + convertir_romano_a_decimal (num, pos + 1, n_romanos)
print (convertir_romano_a_decimal ('MCMLXXIV', 0, n_romanos))



# 22 - El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. 
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” 
# realizar las siguientes actividades: 
# 
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila; 
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo; 
# c. Utilizar un vector para representar la mochila.





# 23 - Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una matriz de [n x n], 
# solo se puede mover de a una casilla a la vez –no se puede mover en diagonal– y que la misma sea adyacente y no esté marcada como pared. 
# Se comenzará en la casilla (0, 0) y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, 
# cuando no se pueda avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.


