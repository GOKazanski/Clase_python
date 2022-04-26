# 6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.

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
elemento_contar = input('ingrese la letra que desea contar ')
contador = 0

for i in range(c.tamanio()):
    if (elemento_contar == c.mover_al_final()):
        contador += 1

print('cantidad de ocurrencias', contador)
