#3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from pila import pila
from random import randint

pila1 = pila()
pila_aux = pila()

x = int(input('ingrese el numero a reemplazar '))
aux = 100

for i in range(5):
    num = randint(1, 3)
    print(num)
    pila1.apilar(num)

while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    if(dato == x):
        pila_aux.apilar(aux)
    else:
        pila_aux.apilar(dato)

while(not pila_aux.pila_vacia()):
    dato = pila_aux.desapilar()
    pila1.apilar(dato)

print ()
print ('Nueva Lista')
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    print(dato)