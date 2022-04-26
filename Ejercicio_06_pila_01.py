#1. Determinar el número de ocurrencias de un determinado elemento en una pila.

from pila import pila
from random import randint

pila1 = pila()
contador = 0

x = int(input('ingrese el numero que desae contar ocurrencias '))

for i in range(10):
    num = randint(1, 5)
    print(num)
    pila1.apilar(num)


while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    if(dato == x):
        contador += 1

print('cantidad de ocurrencias:', contador)