#
#vec = [1, 3, 4, 5, 70, 100] 
#
#def busqueda_secuencial(vector, buscado, indice):
#    if(indice == len(vec)):
#        return -1
#    elif(buscado == vector[indice]):
#        return indice
#    else:
#        return busqueda_secuencial(vector, buscado, indice+1)
#
#def busqueda_secuencial2(vector, buscado):
#    if(len(vector) == 0):
#        return -1
#    elif(buscado == vector[-1]):
#        return len(vector)-1
#    else:
#        return busqueda_secuencial2(vector[:-1], buscado)
#
#print(busqueda_secuencial2(vec, 33))
#
#
#def contar_digitos(numero):
#    if(numero < 10):
#        return 1
#    else:
#        return 1 + contar_digitos(numero//10)
#
#print(contar_digitos(7845))
#
#
#cadena = 'hola'
#
#def invertir_cadena(cadena, indice):
#    if(indice == 1):
#        return cadena[indice-1]
#    else:
#        return cadena[indice-1] + invertir_cadena(cadena, indice-1)
#
#def invertir_cadena2(cadena):
#    if(len(cadena) == 0):
#        return cadena
#    else:
#        return cadena[-1] + invertir_cadena2(cadena[:-1])
#
## print(invertir_cadena2(cadena))
#
#def sumatoria(numero):
#    if(numero == 1):
#        return numero
#    else:
#        return 1/numero + sumatoria(numero-1)
#
#print(sumatoria(3))
#
#def suma(num):
#    if(num == 0):
#        return num
#    else:
#        return num + suma(num-1)
#
#
## print(suma(5))
#
#
## 2^3 = 2 * 2 * 2
#
#def potencia(base, exponente):
#    if(exponente == 0):
#        return 1
#    else:
#        return base * potencia(base, exponente-1)
#
#
## print(potencia(2,5))
#
#def factorial_iterativa(num):
#    factorial = 1
#    for n in range(2, num+1):
#        factorial = factorial * n
#    
#    return factorial
#
#def factorial_recursivo(num):
#    if(num == 0):
#        # print('se alcanzo condicion de fin')
#        return 1
#    else:
#        # print('antes de la llamada recursiva num:', num)
#        # value = num * factorial_recursivo(num-1)
#        # print('despues de la llamada recursiva num:', value)
#        # return value
#        return num * factorial_recursivo(num-1)
#
#
#def fib_iter(num):
#    val1 = 0
#    val2 = 1
#    for n in range(2, num+1):
#        resultado = val1 + val2
#        val1 = val2
#        val2 = resultado
#    return resultado
#
#
#def fib_rec(num):
#    if(num == 0 or num == 1):
#        return num
#    else:
#        return fib_rec(num-1) + fib_rec(num-2)
#
## print(factorial_recursivo(5))
## print(factorial_iterativa(5))
#
#
## for i in range(2, 11):
##     print('fibanacci ', i, fib_rec(i))
#
#
#
##! 2 4 6 7 10 20 

#vec =[1, 3, 4, 5, 11, 30, 70, 100]
#
#def bbinaria(vector, buscado, primero, ultimo):
#    medio =(primero + ultimo)//2
#    if (primero > ultimo):
#        return -1
#    elif (buscado == vector[medio]):
#        return medio
#    elif (vector[medio]<buscado):
#        bbinaria (vector, buscado, medio+1, ultimo)
#    else:
#        bbinaria (vector, buscado, primero, medio-1)
#
#print ('posicion:', bbinaria(vec, 11, 0, len(vec)-1))
#
#
#matriz = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
#    ]
#
#for i in range(len(matriz)):
#    for j in range(len(matriz[i])):
#        print(matriz[i][j])
#
















