#17. Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

vec=[0, 1, 2, 4, 5, 6, 8, 9, 10]

def barrido_descendente(vec):
    if (len(vec)==1):
        print(vec[0])
    else:
        print (vec[len(vec)-1])     #print (vec[-1])
        barrido_descendente (vec[:-1])

def barrido_descendente_b(vec,pos):
    if(pos==0):
        print(vec[pos])
    else:
        print(vec[pos])
        barrido_descendente_b(vec,pos-1)

print (vec)
barrido_descendente(vec)
print()
barrido_descendente_b (vec,8)


