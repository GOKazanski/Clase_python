# 5 - Desarrollar una función que permita convertir un número romano en un número decimal.

nromanos = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1} #Diccionario

def convertir_romano_a_decimal (num, pos, nromanos):
    if (pos==(len(num)-1)):
        return nromanos[num[pos]]
    else:
        romana_actual = nromanos [num[pos]] #guarda el valor de la letra de la izquierda en la variable
        romana_siguiente = nromanos [num[pos + 1]] #guarda el valor de la letra siguiente
        if (romana_actual < romana_siguiente): # si la 1° es memor, resta a la siguiente
            return - romana_actual + convertir_romano_a_decimal (num, pos + 1, nromanos)
        else:
            if (romana_actual >= romana_siguiente): #si la 1° es mayor o igual la suma
                return romana_actual + convertir_romano_a_decimal (num, pos + 1, nromanos)
            
print (convertir_romano_a_decimal ('MCMLXXIV', 0, nromanos))
print()

# 22 - El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. 
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” 
# realizar las siguientes actividades: 
# 
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila; 
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo; 
# c. Utilizar un vector para representar la mochila.

mochila_jedi = ['manta', 'casco','escudo','sable de luz', 'kimono']

def usar_la_fuerza (mochila_jedi, pos):
    if (pos < len(mochila_jedi)):
        if (mochila_jedi [pos]=='sable de luz'):
            print()
            print ('El Sable de Luz salió estaba en la mochila y salió en la posición: ', pos + 1)
        else:
            print(mochila_jedi[pos])
            return usar_la_fuerza (mochila_jedi, pos + 1)
    else:
        print()
        print ('El sable de luz no está en la mochila')
        
print (usar_la_fuerza (mochila_jedi,0))
print()
        
# 23 - Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una matriz de [n x n], 
# solo se puede mover de a una casilla a la vez –no se puede mover en diagonal– y que la misma sea adyacente y no esté marcada como pared. 
# Se comenzará en la casilla (0, 0) y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, 
# cuando no se pueda avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

laberinto = [[ 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
            [  1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
            [  0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [  0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [  1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [  1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [  1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            [  1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
            [  1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
            [  1, 1, 1, 1, 0, 2, 1, 1, 0, 1]]
       
def salida_del_laberinto (matriz, x, y, recorrido = []):
    if (x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if (matriz [x][y]==2):#pregunta si el elemento es la salida "2"
            recorrido . append ([x,y])
            print ('ha encontrado la salida del laberinto')
            print (recorrido)
            recorrido . pop ()
        elif (matriz [x] [y]== 1):
            matriz [x] [y]= 3
            recorrido . append ([x,y])
            salida_del_laberinto (matriz, x, y+1, recorrido)
            salida_del_laberinto (matriz, x, y-1, recorrido)       
            salida_del_laberinto (matriz, x-1, y, recorrido)       
            salida_del_laberinto (matriz, x+1, y, recorrido)       
            recorrido . pop ()
            matriz [x][y]=1

print ( salida_del_laberinto(laberinto, 0, 0))
