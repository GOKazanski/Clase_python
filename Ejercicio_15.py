import os

os.system('clear')

"""
15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos
    ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los
    cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades utilizando lista de lista
    implementando las funciones necesarias: 
    a. obtener la cantidad de Pokémons de un determinado entrenador; 
    b. listar los entrenadores que hayan ganado más de tres torneos;
    c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
    d. mostrar todos los datos de un entrenador y sus Pokémos;
    e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
    f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
    g. el promedio de nivel de los Pokémons de un determinado entrenador;
    h. determinar cuántos entrenadores tienen a un determinado Pokémon;
    i. mostrar los entrenadores que tienen Pokémons repetidos;
    j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull; 
    k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon
       deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
"""

from lista import Lista
from random import randint, choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        return self.nombre

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'uno', 'tg': 15, 'bg': 45,  'bp': 11},
    {'name': 'dos', 'tg': 3, 'bg': 12,  'bp': 35},
    {'name': 'tres', 'tg': 0, 'bg': 50,  'bp': 50},
    {'name': 'cuatro', 'tg': 1, 'bg': 10,  'bp': 1},
    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemons = [
    {'name': 'pok1', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'pok2', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'pok3', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'pok4', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'pok5', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'pok6', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]

for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tg'],
                                           entrenador['bp'],
                                           entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista() 
 
# a. obtener la cantidad de Pokémons de un determinado entrenador; 
print()
print('PUNTO A: obtener la cantidad de Pokémons de un determinado entrenador')
print()
entrenador = input('ingrese nombre del entrenador: ')
print()
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
else:
    print('el entrenador no esta en la lista')

# b. listar los entrenadores que hayan ganado más de tres torneos;
print()
print('PUNTO B: listar los entrenadores que hayan ganado más de tres torneos')
print()
lista_entrenadores.barrido_entrenador_mas_tres()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print()
print('PUNTO C: el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados')
print()
mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print(mayor.info, mayor.sublista.mayor_de_lista('nivel').info)

# d. mostrar todos los datos de un entrenador y sus Pokémos;
print()
print('PUNTO D: mostrar todos los datos de un entrenador y sus Pokémos')
print()
entrenador = input('ingrese nombre del entrenador: ')
print()
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"el entrenador: {pos.info}")
    print('sus pokemons')
    pos.sublista.barrido()
else:
    print('el entrenador no esta en la lista')

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print()
print('Punto E: mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %')
print()
lista_entrenadores.barrido_porcentaje_victorias()

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print()
print('Punto F: los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)')
print()
lista_entrenadores.barrido_entrenador_tipo()

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print()
print('PUNTO G: el promedio de nivel de los Pokémons de un determinado entrenador')
print()
entrenador = input('ingrese nombre del entrenador: ')
print()
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print('Listado de pokémones')
    pos.sublista.barrido()
    print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
    print(f"El promedio es: {pos.sublista.suma_de_nivel()/pos.sublista.tamanio()}")
else:
    print('el entrenador no esta en la lista')

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print()
print('PUNTO H: determinar cuántos entrenadores tienen a un determinado Pokémon')
print()
buscado = input('Ingresar en Nombre del Pokémon: ')
print()
lista_entrenadores.barrido_lista_pokebuscado(buscado)
      
# i. mostrar los entrenadores que tienen Pokémons repetidos;
print()
print('PUNTO I: mostrar los entrenadores que tienen Pokémons repetidos')
print()
lista_entrenadores.barrido_pokemon_repetido()

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
#print()
#print('PUNTO J: determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull')
#print()

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon
#  deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
print()
print('PUNTO K: determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon')
print('         deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos')
print()
entrenador = input('Ingrese nombre del entrenador: ')
buscado = input('Ingresar en Nombre del Pokémon: ')
print()
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    pospok=pos.sublista.busqueda(buscado,'nombre')
    if (pospok):
        print(f"el entrenador: {pos.info}, tiene el pokemon: {pospok.info}")
    else:
        print('El entrenador no posee ese Pokémon')
else:
    print('El entrenador no esta en la lista')
print()
