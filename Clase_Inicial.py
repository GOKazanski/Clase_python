

#! mostrar algo en la consola
#! int str bool float complex None

numero = 8
print(type(numero))
numero = 19.7
print(type(numero))
numero = 'holañ'
print(type(numero), len(numero), numero)
numero = True
print(type(numero))

#! conversion de tipos cast:   int() str() foat() bool()
#! operadores aritmeticos + - * / // %(mod) **
# numero = int(input('ingrese un numero '))

# print('lo que quieran mostrar', 'otra cosa', numero * 2)

n1 = 2
n2 = 10

# print(n1 ** n2)

#! condicional  if  if-else  elif
#! operadores de control > < >= <= == !=


if(n2 > 0):
    print('positivo')
elif(n2 < 0):
    print('es negativo')
else:
    print('es neutro')

#! ciclos  while - for  !=


# while(n2 > 0 and n2 != 4):
#     print('valor:', n2)
#     n2 -= 1


#! operadores logicos and or not ^


#! estructuras de datos array --> listas  diccionarios 

vec = [1, 3, 6, 7, 0, 45, 'hola', True]
# vec.insert(4, 'algo')
# vec.append(input('ingrese un numero: '))  #* agregar
# vec.remove(6)   #* eliminar
# print(vec, len(vec))
# vec[0] = 2
# print(vec)
# for i in range(0, len(vec)):
#     print(vec[i])
for elemento in vec:
    print(elemento)


#! funcion

v1 = 12
v2 = 5

def mi_funcion(valor1, valor4, *otros):
    print('lo que haga mi funcion')
    print('lista argumentos')
    for elemento in otros:
        print(elemento)


print(vec)
mi_funcion(v1, v2, 76, 45, 67 , 89 , 0)

print(v1, v2, vec)


from mi_modulo import suma


print(suma(3, 7))