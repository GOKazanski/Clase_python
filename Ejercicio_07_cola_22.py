# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, 
# el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from cola import Cola
from random import randint

class  Personajes ( object ):
    def  __init__ ( self , NombrePersonaje , NombreHeroe , Genero ):
        self.NombrePersonaje  =  NombrePersonaje 
        self.NombreHeroe  =  NombreHeroe
        self.Genero  =  Genero

    def  __str__ ( self ):
        return self.NombrePersonaje  + '-' + self . NombreHeroe + '-' + self . Genero
    
C = Cola()
CFemenino=Cola()
CMasculino=Cola()

personajes = Personajes ("Tony Stark", "Iron Man", "M")
C.arribo (personajes)
personajes = Personajes ("Steve Rogers", "Capitán América", "M")
C.arribo (personajes)
personajes = Personajes ("Natasha Romanoff", "Black Widow", "F")
C.arribo (personajes)
personajes = Personajes ("Carol Danvers","Capitana Marvel" , "F")
C.arribo (personajes)
personajes = Personajes ("AntMan","Scott Lang" ,"M" )
C.arribo (personajes)

while(not C.cola_vacia()):
    x=C.atencion()
    # a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
    if (x.NombreHeroe == "Capitana Marvel"):
        print()
        print("Nombre de la capitana Marvel:" , x.NombrePersonaje)
        
    # b. mostrar los nombre de los superhéroes femeninos;
    if (x.Genero=="F"):
        CFemenino.arribo(x)

    # c. mostrar los nombres de los personajes masculinos;
    if (x.Genero=="M"):
        CMasculino.arribo(x)

    # d. determinar el nombre del superhéroe del personaje Scott Lang;
    if (x.NombreHeroe == "Scott Lang"):
        print("Nombre de Scott Lang:" , x.NombrePersonaje)
        print("")

    # e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
    if (x.NombrePersonaje[0] == "S" or x.NombreHeroe[0] == "S"):
        print("Datos de personajes que comienzan con S")
        print(x)
        print()
        
    # f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
    if (x.NombrePersonaje == "Carol Danvers"):
        print()
        print("La personaje Carol Danvers se encuentra en la cola")
        print("su nombre de super heroe es: " , x.NombreHeroe)

# b. mostrar los nombre de los superhéroes femeninos;
print("Personajes femeninos")
while(not CFemenino.cola_vacia()):
    x=CFemenino.atencion()
    print(x.NombrePersonaje)
    
# c. mostrar los nombres de los personajes masculinos;
print("")
print("Personajes masculinos")
while(not CMasculino.cola_vacia()):
    x=CMasculino.atencion()
    print(x.NombrePersonaje)