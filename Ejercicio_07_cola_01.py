#1. Eliminar de una cola de caracteres todas las vocales que aparecen.

from cola import Cola

vocales = ['A', 'E', 'I', 'O', 'U']

def random_character():
    from random import randint
    return chr(randint(65, 90)) #! mayuscula

c = Cola()

for i in range(20):
    dato = random_character()
    c.arribo(dato)
    print(dato)

print()


for i in range(c.tamanio()):
    dato = c.atencion()
    if(dato not in vocales):
        c.arribo(dato)
    else:
        print('dato eliminado', dato)

print()


# for i in range(c.tamanio()):
#     print(c.mover_al_final())