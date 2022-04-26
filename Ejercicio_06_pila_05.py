#5. Determinar si una cadena de caracteres es un palíndromo.

from pila import pila
from random import randint

pila1 = pila()
pila_invertida = pila()
pila_2 = pila()

palabra = input('ingrese un palabra ')

for letra in palabra:
    pila1.apilar(letra)

while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    pila_invertida.apilar(dato)
    pila_2.apilar(dato)

while(not pila_2.pila_vacia()):
     pila1.apilar(pila_2.desapilar())

while(not pila1.pila_vacia() and (pila1.cima() == pila_invertida.cima())):
    pila1.desapilar()
    pila_invertida.desapilar()

if(pila1.pila_vacia()):
    print('la palabra es un palindromo')
else:
    print('no es un palindromo', pila1.tamanio())