def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]

class nodoLista():
    info, sig, sublista = None, None, None

class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0

    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig
        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig

        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            aux = aux.sig
            print()



# Ejercicio 6
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig

    def barrido_anterior_1963(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.aparicion < 1963):
                print(aux.info)
            aux = aux.sig

    def contar_por_casa(self):
        marvel, dc = 0, 0
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.casa.capitalize() == 'Marvel'):
                marvel += 1
            if(aux.info.casa.capitalize() == 'Dc'):
                dc += 1
            aux = aux.sig
        return marvel, dc    



# Ejercicio 15

    # PUNTO E
    def barrido_porcentaje_victorias(self):
        aux = self.__inicio
        while(aux is not None):
            total = aux.info.batallas_ganadas + aux.info.batallas_perdidas
            if(aux.info.batallas_ganadas / total >= 0.79):
                print(aux.info)
            aux = aux.sig

    # PUNTO B
    def barrido_entrenador_mas_tres(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados > 3):
                print(aux.info)
            aux = aux.sig

    # PUNTO F
    def barrido_entrenador_tipo(self):
        aux = self.__inicio
        while(aux is not None):
            aux1 = aux.sublista.__inicio
            while (aux1 is not None):
                if ('planta' in aux1.info.tipo and 'tierra' in aux1.info.subtipo):
                    print(aux.info)
                    break
                aux1 = aux1.sig
            aux = aux.sig

    # PUNTO C
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
                break
            aux = aux.sig
        return mayor

    # PUNTO G
    def suma_de_nivel(self):
        aux = self.__inicio
        total=0
        while(aux is not None):
            total=(aux.info.nivel)+total
            aux = aux.sig
        return total

    # PUNTO H
    def barrido_lista_pokebuscado(self,buscado):
        aux = self.__inicio
        while(aux is not None):
            aux1 = aux.sublista.__inicio
            aux2 = 0
            while (aux1 is not None):
                if (buscado in aux1.info.nombre):
                    print(aux.info)
                    aux2 = aux2 + 1
                    break
                aux1 = aux1.sig
            aux = aux.sig
        if aux2 == 0:
            print('No se encuentra ese Pokémon')
                       
    # PUNTO I
    def barrido_pokemon_repetido(self):
        aux = self.__inicio
        while(aux is not None):
            aux1 = aux.sublista.__inicio
            while (aux1 is not None):
                aux2=aux1.info.nombre  #guarda en nombre del pokemon
                aux3=aux.sig #el valor del siguiente entrenador
                while(aux3 is not None):
                    aux4=aux3.sublista.__inicio
                    while(aux4 is not None):
                        if(aux2 == aux4.info.nombre):
                            print(f"El entrenador:{aux.info} y el entrenador:{aux3.info} tienen el pokémon {aux2}")
                        aux4=aux4.sig
                    aux3=aux3.sig
                aux1 = aux1.sig
            aux = aux.sig



# Ejercicio 21

    #PUNTO A
    def barrido_anio(self,campo):
        contador=0
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.anio==campo):
                print(aux.info)
                contador = contador + 1
            aux = aux.sig
        if contador==0:
            print('No hay peliculas para ese anio.')

    #PUNTO B
    def mayor_recaudacion(self):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(float(aux.info.recaudacion) > float(mayor.info.recaudacion)):
                mayor = aux
            aux = aux.sig
        return mayor   

    #PUNTO C
    def mayor_valor(self):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.valor) > (mayor.info.valor):
                mayor = aux
            aux = aux.sig
        return mayor        

    def barrido_valor(self,mayorvalor):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.valor) == (mayorvalor):
                print(aux.info)
            aux = aux.sig

# Ejercicio 22

    #PUNTO D
    def barrido_jedi_master(self):
        aux = self.__inicio
        while(aux is not None):
            if('yoda' in aux.info.maestro or 'luke skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig
    
    #PUNTO E
    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig

    #PUNTO F
    def barrido_sable_de_luz(self):
        aux = self.__inicio
        while(aux is not None):
            if(len(aux.info.sable_luz)>1):
                print(aux.info)
            aux = aux.sig

    #PUNTO G
    def barrido_sable_Y_V(self):
        aux = self.__inicio
        while(aux is not None):
            if('yellow' in aux.info.sable_luz or 'purple' in aux.info.sable_luz):
                print(aux.info)
            aux = aux.sig
