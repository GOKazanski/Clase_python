# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, 
#  desarrollar las funciones necesarias para resolver las siguientes actividades: 
# a. mostrar los nombre películas estrenadas en el año 2014; 
# b. indicar cuántas películas se estrenaron en el año 2018; 
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from pila import Pila
from random import choice

pila1 = Pila()

class Film():
    pelicula, estudio, anio = None, None, None

pelicula = ['iron man I', 'iron man II','iron man III', 'Avengers1', 'Spider-Man', 'Capitan America']
estudio = ['Marvel','Pixar']
anio = ['2014','2016','2017','2018']


print()

for i in range(len(pelicula)):
    dato = Film()
    dato.pelicula = pelicula[i]
    dato.estudio = choice(estudio)
    dato.anio = choice(anio)
    dic = {'pelicula': pelicula[i], 'estudio': choice(estudio), 'anio':choice(anio)}
    print(dato.pelicula, dato.estudio,dato.anio)
    pila1.apilar(dato)

contador=0
print ()
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()

# a. mostrar los nombre películas estrenadas en el año 2014; 
    if(dato.anio == '2014'):
        print('Pelicula estrenada en el 2014: ', dato.pelicula)

# b. indicar cuántas películas se estrenaron en el año 2018; 
    if(dato.anio == '2018'):
        contador += 1

# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
    if(dato.anio == '2016' and dato.estudio == 'Marvel'):
        print('Pelicula estrenada en el 2016 por Marvel: ', dato.pelicula)

print()
print('cantidad de peliculas del 2018 son: ', contador)
print()