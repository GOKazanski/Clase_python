# 22 - El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. 
# Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” 
# realizar las siguientes actividades: 
# 
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila; 
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo; 
# c. Utilizar un vector para representar la mochila.

mochila_jedi = ['manta', 'casco','escudo','sable de luz', 'kimono']

def usar_la_fuerza (mochila_jedi, pos):
    if (pos < len(mochila_jedi)):
        if (mochila_jedi [pos]=='sable de luz'):
            print()
            print ('El Sable de Luz salió estaba en la mochila y salió en la posición: ', pos + 1)
        else:
            print(mochila_jedi[pos])
            return usar_la_fuerza (mochila_jedi, pos + 1)
    else:
        print()
        print ('El sable de luz no está en la mochila')
        
print (usar_la_fuerza (mochila_jedi,0))
print()