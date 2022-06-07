# 18. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
# letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
# que resuelva las siguientes situaciones:
# 
# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C y F, y la cola_2 con el resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506.

from cola import Cola
from random import randint

def random_character():
    return chr(randint(65, 70)) #! mayuscula

c = Cola()
cola_1 = Cola()
cola_2 = Cola ()
c1aux= Cola()
c2aux= Cola ()


# a. cargar 1000 turnos de manera aleatoria a la cola.
print('Cola de Turnos Principal')
for i in range(11):
    dato = random_character() + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
    c.arribo(dato)
    print(dato)

print()

# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C y F,
#  y la cola_2 con el resto de los turnos (B, D y E).

while (not c.cola_vacia()):
    dato1 = c.atencion()
    if (dato1[0]=='A' or dato1[0]=='C' or dato1[0]=='F'):
        cola_1.arribo(dato1)
        c1aux.arribo(dato1)
        #print('Lista 1: ',dato1)
    else:
        cola_2.arribo(dato1)
        c2aux.arribo(dato1)
        #print('Lista 2:',dato1)

# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras tiene mayor cantidad.
print('tamanio cola 1:',cola_1.tamanio())
print('tamanio cola 2:',cola_2.tamanio())
print()
letra_A=0
letra_C=0
letra_F=0
letra_B=0
letra_D=0
letra_E=0

if (cola_1.tamanio()==cola_2.tamanio()):
    print('Las colas tienen el mismo tamaño')
else:
    if (cola_1.tamanio()>cola_2.tamanio()):
        print('La cola 1 es mayor')
        while (not cola_1.cola_vacia()):
            dato1=cola_1.atencion()
            if(dato1[0]=="A"):
                letra_A += 1
            else:
                if(dato1[0]=="C"):
                    letra_C +=1
                else:
                    letra_F +=1

        if(letra_A > letra_C and letra_A > letra_F): 
            print('Los turnos A tiene mas cantidad:',letra_A)
        else:
            if(letra_C > letra_F and letra_C > letra_A):
                print('Los turnos C tienen mas cantidad:',letra_C)
            else:
                print('Los turnos F tienen mas cantidad:',letra_F)
    else:
        print('la cola 2 es mayor')
        while (not cola_2.cola_vacia()):
            dato2=cola_2.atencion()
            if(dato2[0]=="B"):
                letra_B +=1
            else:
                if(dato2[0]=="D"):
                    letra_D +=1
                else:
                    letra_E +=1
                
        if(letra_B > letra_D and letra_B > letra_E):
            print('Los turnos B tiene mas cantidad:',letra_B)
        else:
            if(letra_D > letra_E and letra_D > letra_B):
                print('Los turnos D tienen mas cantidad:',letra_D)
            else:
                print('Los turnos E tienen mas cantidad:',letra_E)

# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506.
print()

if (c1aux.tamanio()==c2aux.tamanio()):
    print('Las colas tienen el mismo tamaño')
else:
    if (c1aux.tamanio()<c2aux.tamanio()):
        print('La cola 1 es menor')
        while (not c1aux.cola_vacia()):
            dato1=c1aux.atencion()
            #print(dato1)
            dato2=int(dato1[1:4])
            if(dato2>506):
                print('Los turnos mayores a 506 son:',dato1)
    else:
        print('La cola 2 es la menor')
        while (not c2aux.cola_vacia()):
            dato1=c2aux.atencion()
            print(dato1)
            #dato2=int(dato1[1:4])
            if(dato2>506):
                print('Los turnos mayores a 506 son:',dato1)


