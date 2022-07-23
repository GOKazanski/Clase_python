import os

os.system('clear')

"""
22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
    colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
    actividades enumeradas a continuación:
    a. listado ordenado por nombre y por especie;
    b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
    c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
    d. mostrar los Jedi de especie humana y twi'lek;
    e. listar todos los Jedi que comienzan con A;
    f. mostrar los Jedi que usaron sable de luz de más de un color;
    g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
    h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
"""
from lista import Lista

class Jedi:
    
    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"

lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('/home/gabriel/Documentos/2° año/Algoritmos/Clase_python/08_Lista_Ejercicios/jedis.txt')
lineas = file.readlines()

lista = []

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    datos.pop(-1)
    # print(datos[4].split('/'))
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),
                        campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         campo='especie')
    lista.append(Jedi(datos[0],
                      datos[2],
                      datos[3].split('/'),
                      datos[4].split('/')))

# a. listado ordenado por nombre y por especie;
print('PUNTO A. listado ordenado por nombre y por especie')
print()
lista_jedi.barrido()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
print()
print('PUNTO B. mostrar toda la información de Ahsoka Tano y Kit Fisto;')
print()
dato = lista_jedi.busqueda('kit fisto', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print()
print('PUNTO C. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices')
print ()
dato = lista_jedi.busqueda('yoda', 'nombre')
if dato:
    print(f'Los padawans del Jedi {dato.info.nombre} son, {dato.info.maestro}')
else:
    print('el Jedi no esta en la lista')
dato = lista_jedi.busqueda('luke skywalker', 'nombre')
if dato:
    print(f'Los padawans del Jedi {dato.info.nombre} son, {dato.info.maestro}')
else:
    print('el Jedi no esta en la lista')

# d. mostrar los Jedi de especie humana y twi'lek;
print()
print('PUNTO D. mostrar los Jedi de especie humana y twilek')
print()
lista_jedi.barrido_jedi_master()

# e. listar todos los Jedi que comienzan con A;
print()
print('PUNTO E. listar todos los Jedi que comienzan con A')
print()
lista_jedi.barrido_comienza_con(['a'])

# f. mostrar los Jedi que usaron sable de luz de más de un color;
print()
print('PUNTO F. mostrar los Jedi que usaron sable de luz de más de un color')
print()
lista_jedi.barrido_sable_de_luz()

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print()
print('PUNTO G. indicar los Jedi que utilizaron sable de luz amarillo o violeta')
print()
lista_jedi.barrido_sable_Y_V()

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print()
print('PUNTO H. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.')
print()
dato = lista_jedi.busqueda('qui-gon jin', 'nombre')
if dato:
    print(f'Los padawans del Jedi {dato.info.nombre} son, {dato.info.maestro}')
else:
    print('el Jedi no esta en la lista')
dato = lista_jedi.busqueda('mace windu', 'nombre')
if dato:
    print(f'Los padawans del Jedi {dato.info.nombre} son, {dato.info.maestro}')
else:
    print('el Jedi no esta en la lista')
print()