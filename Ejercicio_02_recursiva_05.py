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