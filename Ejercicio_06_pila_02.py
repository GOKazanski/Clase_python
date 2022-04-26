#2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.

from pila import pila
from random import randint

pila1 = pila()
pila_aux = pila()

for i in range(10):
    num = randint(1, 6)
    print(num)
    pila1.apilar(num)

while(not pila1.pila_vacia()):
    dato = pila1.desapilar()#

    if(dato % 2 == 0):
        pila_aux.apilar(dato)

while(not pila_aux.pila_vacia()):
    dato = pila_aux.desapilar()
    pila1.apilar(dato)

print('elementos pares')
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    print(dato)