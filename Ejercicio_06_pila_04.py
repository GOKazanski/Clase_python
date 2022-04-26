#4.Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

from pila import pila
from random import randint

pila1 = pila()
pila_aux = pila()

for i in range(5):
    num = randint(1, 10)
    print(num)
    pila1.apilar(num)

while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    pila_aux.apilar (dato)

print ()
print ('Nueva Lista')
while(not pila_aux.pila_vacia()):
    dato = pila_aux.desapilar()
    print(dato)
