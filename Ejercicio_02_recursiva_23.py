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
            matriz [x] [y]= 3 #Cambia el valor de la posición a 3
            recorrido . append ([x,y])
            salida_del_laberinto (matriz, x, y+1, recorrido)#recorrido hacia la derecha
            #print ("▶")
            salida_del_laberinto (matriz, x, y-1, recorrido)#recorrido hacia la izquierda
            #print ("◀")       
            salida_del_laberinto (matriz, x-1, y, recorrido)#recorrido hacia arriba
            #print ("▲")
            salida_del_laberinto (matriz, x+1, y, recorrido)#recorrido hacia abajo
            #print ("▼")
            recorrido . pop ()
            matriz [x][y]=1

print ( salida_del_laberinto(laberinto, 0, 0))