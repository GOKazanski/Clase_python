from jurassic_park import dinosaurs
from Parcial_Lista import Lista
from Parcial_Cola import Cola

class Dino:
    
    #time;zone_code;dino_number;alert_level
    #{'name': 'Tyrannosaurus Rex', 'type': 'carnívoro ', 'number': 8,'period': 'cretácico superior', 'named_by': 'Osborn, 1905'},
    
    def __init__(self, time, zone_code, dino_number, alert_level, name, type, number, period, named_by):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by = named_by
      
    def __str__(self):
        return f"{self.time} - {self.zone_code} - {self.dino_number} - {self.alert_level} - {self.name} - {self.type} - {self.number} - {self.period} - {self.named_by}"

def busqueda1(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']

def busqueda2(buscado):
    for dino in dinosaurs:
        if(buscado == dino['name']):
            return dino['type']

def busqueda3(buscado):
    for dino in dinosaurs:
        if(buscado == dino['name']):
            return dino['number'] 

def busqueda4(buscado):
    for dino in dinosaurs:
        if(buscado == dino['name']):
            return dino['period'] 

def busqueda5(buscado):
    for dino in dinosaurs:
        if(buscado == dino['name']):
            return dino['named_by']         

file =open('/home/gabriel/Documentos/2° año/Algoritmos/Clase_python/Parciales/alerts.txt')

lineas = file.readlines()
lineas.pop(0)
#print(lineas)
lista_dinosaurs = Lista()
lista_dino2=Lista()
lista_jurasica=Lista()
lista_total=Lista()

for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda1(dato[2]))
    dato.append(busqueda2(dato[4]))
    dato.append(busqueda3(dato[4]))
    dato.append(busqueda4(dato[4]))
    dato.append(busqueda5(dato[4]))
    lista_dinosaurs.insertar(Dino(dato[0],
                                    dato[1],
                                    dato[2],
                                    dato[3],
                                    dato[4],
                                    dato[5],
                                    dato[6],
                                    dato[7],
                                    dato[8].split(', ')),'time')
    lista_dino2.insertar(Dino(dato[0],
                                dato[1],
                                dato[2],
                                dato[3],
                                dato[4],
                                dato[5],
                                dato[6],
                                dato[7],
                                dato[8].split(', ')),'name')

print()
print('el ultimo dinosaurio descubierto')



print() 
print('listado por hora')
#lista_dinosaurs.barrido()

print()
print('listado por monbre')
#lista_dino2.barrido()

print()
print('eliminacion zonas WYG075, SXH966 y LYF010')
dato = lista_dinosaurs.eliminar('WYG075','zone_code')
dato = lista_dino2.eliminar('WYG075','zone_code')
dato = lista_dinosaurs.eliminar('SXH966','zone_code')
dato = lista_dino2.eliminar('SXH966','zone_code')
dato = lista_dinosaurs.eliminar('LYF010','zone_code')
dato = lista_dino2.eliminar('LYF010','zone_code')

print()
print('zona HYD195 el nombre correcto del dinosaurio es Mosasaurus.')
dato = lista_dinosaurs.busqueda('HYD195', 'zone_code')
if dato:
    dato.info.name = 'Mirta_Legran'
    print(f'el dinosaurio de la zona {dato.info.zone_code} fue modificado')
else:
    print('la zona no esta en la lista')

#lista_dinosaurs.barrido()

#filtrado de los datos que solo incluya datos de los dinosaurios: 
# Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel ´critical’ o ‘high’
print()
print('Lista dinos con alarma')
lista_dinosaurs.barrido_dino_alarma()

Cola0=Cola()
Cola1=Cola()
Cola2=Cola()

#dos colas, una con los datos de dinosaurios carnívoros y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’
print()
#print(lista_dinosaurs.tamanio())

for i in range(lista_dinosaurs.tamanio()):
    dino=lista_dinosaurs.obtener_elemento(i)
    if ('critical' in dino.alert_level or 'high' in dino.alert_level):
        if ('carnívoro' in dino.type):
            Cola1.arribo(dino)
        else:
            if ('herbívoro' in dino.type):
                Cola2.arribo(dino)

print()
print("dinosaurios carnívoros")
while(not Cola1.cola_vacia()):
    x=Cola1.atencion()
    print(x)

print()
print("dinosaurios herbívoro")
while(not Cola2.cola_vacia()):
    x=Cola2.atencion()
    print(x)

# un listado de toda la información que tienen procesada del archivo, pero solo de los dinosaurios
#  Raptors y Carnotaurus; y los códigos de las zonas donde puedo encontrar dinosaurios Compsognathus
print()
print('Lista dinos Raptors y Carnotaurus')
lista_dinosaurs.barrido_Rap_Car()
print()
print('Lista de las zonas donde puedo encontrar dinosaurios Compsognathus')
lista_dinosaurs.barrido_Zona_Comp()

# Clave mosquito
# 1. si el número está entre 33 y 47 su valor alfanumérico esta ok.
# 2. caso contrario
#       si número es divisible por 3 entonces (número // 2) + 9 (es tu nuevo valor alfanumérico)
#       sino número -14 (es tu nuevo valor alfanumérico)
#   
#       en cualquiera de los casos debes continuar procesandolo, es una solución parcial.
#
#  3. al final obtendrás la clave si sabes cómo hacer las cosas, pero recuerda ‘mosquito’ es la clave de todo.

print()
print ('La clave mosquito')


print()
