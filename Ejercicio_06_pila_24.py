# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre 
# y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades: 

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from pila import Pila
from random import choice

pila1 = Pila()
pila2 = Pila()

class Personajes():
    nombre, cantidad = None, None,

nombre = ['iron man','Black Widow','Spider-Man','Rocket Raccoon','Groot','Capitan America']
cantidad = [4,5,6,7]

print()

for i in range(len(nombre)):
    dato = Personajes()
    dato.nombre = nombre[i]
    dato.cantidad = choice(cantidad)
    dic = {'nombre': nombre[i], 'cantidad':choice(cantidad)}
    print(dato.nombre, dato.cantidad)
    pila1.apilar(dato)
    pila2.apilar(dato)

print()
contador=0

while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    contador += 1
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
    if(dato.nombre == 'Rocket Raccoon'):
        contador1 = contador
    if(dato.nombre == 'Groot'):
        contador2 = contador
        
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
    if(dato.cantidad >= 5):
         print('el personaje: ',dato.nombre,' participo en: ',dato.cantidad)

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    if(dato.nombre == 'Black Widow'):
        datoBW = dato.cantidad
        
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G. 
print()
while(not pila2.pila_vacia()):
    dato = pila2.desapilar()
    if(dato.nombre[0]=="C"):
        print ('personajes que empiezan con C:' , dato.nombre)
    if(dato.nombre[0]=="D"):
        print ('personajes que empiezan con D:' , dato.nombre)
    if(dato.nombre[0]=="G"):
        print ('personajes que empiezan con G:' , dato.nombre)
        
print()
print('Rocket Raccoon esta en la posicion: ', contador1)
print()
print('Groot esta en la posicion: ', contador2)
print()
print('Black Widow participo en: ',datoBW)
print()