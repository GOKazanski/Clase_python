import os

os.system('clear')

"""
21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
    nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación.
    Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
    a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año­–;
    b. mostrar los datos de la película que más recaudo;
    c. indicar las películas con mayor valoración del público, puede ser más de una;
    d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una lista auxiliar–:
       I.      por nombre,
       II.     por recaudación,
       III.    por año de estreno,
       IV.     por valoración del público.
"""

from lista import Lista


class Pelicula:

    def __init__(self, nombre, anio, valor, recaudacion):
        self.nombre = nombre
        self.anio = anio
        self.valor = valor
        self.recaudacion = recaudacion
    
    def __str__(self):
         return f"{self.nombre} - {self.anio} - {self.valor} - {self.recaudacion}"

Lista_de_peliculas = Lista()
Lista_aux= Lista()

dic_peliculas = [
    {'film':'La red social',            'year':'2010','star':'10','many':'   100.00'},
    {'film':'Toy Story 3',              'year':'2010','star':' 7','many':'  2000.00'},
    {'film':'Skyfall',                  'year':'2012','star':' 7','many':' 11851.00'},
    {'film':'Origen',                   'year':'2010','star':' 6','many':'   500.00'},
    {'film':'El Gran Hotel Budapest',   'year':'2014','star':' 6','many':'  4044.00'},
    {'film':'El topo',                  'year':'2011','star':' 5','many':'  2500.00'},
    {'film':'Wonder',                   'year':'2017','star':' 7','many':' 87817.00'},
    {'film':'La invención de Hugo',     'year':'2011','star':' 1','many':'  1700.00'},
    {'film':'Coco',                     'year':'2017','star':'10','many':' 34044.00'},
    {'film':'Gravity',                  'year':'2013','star':' 4','many':' 15454.00'},
    {'film':'Marvel Los Vengadores',    'year':'2012','star':' 8','many':'300000.00'},
    {'film':'Blue Jasmine',             'year':'2013','star':' 3','many':'  5440.00'},
    {'film':'Descifrando Enigma',       'year':'2014','star':' 9','many':' 14464.00'},
    {'film':'Sicario',                  'year':'2015','star':' 4','many':'  5145.00'},
    {'film':'12 años de esclavitud',    'year':'2013','star':' 5','many':'  5814.00'},
    {'film':'Bohemian Rhapsody',        'year':'2018','star':' 9','many':' 84554.00'},
]

for peli in dic_peliculas:
    Lista_de_peliculas.insertar(Pelicula(peli['film'],
                                         peli['year'], 
                                         peli['star'],
                                         peli['many']),'nombre')

Lista_de_peliculas.barrido()

print()
print('PUNTO A. permitir filtrar las películas por año')
aniobuscado = input('Ingrese el año que desea buscar:')
print()
Lista_de_peliculas.barrido_anio(aniobuscado)

print()
print('PUNTO B. mostrar los datos de la película que más recaudo')
mayor = Lista_de_peliculas.mayor_recaudacion()
print(mayor.info)
print()
print('PUNTO C. indicar las películas con mayor valoración del público, puede ser más de una;')
mayor = Lista_de_peliculas.mayor_valor()
estrellas=(mayor.info.valor)
Lista_de_peliculas.barrido_valor(estrellas)

print()
print('PUNTO D. mostrar el contenido de la lista en los siguientes criterios de orden')
print()
opcion=input('Elija una opción: (1)por nombre, (2)por recaudación, (3)por año de estreno, (4)por valoración del público.')
print()

if opcion=='1':
    list_orden='nombre'
elif opcion=='2':
    list_orden='recaudacion'
elif opcion=='3':
    list_orden='anio'
elif opcion=='4':
    list_orden='valor'
else:
    print('Ha colocada una opcion incorrecta')

for peli in dic_peliculas:
    Lista_aux.insertar(Pelicula(peli['film'],
                                peli['year'], 
                                peli['star'],
                                peli['many']),list_orden)

Lista_aux.barrido()
