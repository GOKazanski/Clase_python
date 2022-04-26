#2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.

from cola import Cola
from pila import Pila


def random_character():
    from random import randint
    return chr(randint(65, 90)) #! mayuscula

c = Cola()
pila1 = Pila()

for i in range(5):
    dato = random_character()
    c.arribo(dato)
    print(dato)

for i in range(c.tamanio()):
    dato = c.atencion()
    pila1.apilar(dato)


while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    c.arribo(dato)
print()

for i in range(c.tamanio()):
    dato = c.atencion()
    print (dato)

print()
