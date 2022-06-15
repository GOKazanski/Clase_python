from jurassic_park import dinosaurs
from Parcial_Lista import Lista
from Parcial_Cola import Cola

class Dino:
    
    #time;zone_code;dino_number;alert_level
    #{'name': 'Tyrannosaurus Rex', 'type': 'carnívoro ', 'number': 8,'period': 'cretácico superior', 'named_by': 'Osborn, 1905'},
    
    def __init__(self, time, zone_code, dino_number, alert_level, name):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        self.name = name
        
    
    def __str__(self):
        return f"{self.time} - {self.zone_code} - {self.dino_number} - {self.alert_level} - {self.name} "

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name'] 
 

file =open('/home/gabriel/Documentos/2° año/Algoritmos/Clase_python/Parciales/alerts.txt')

lineas = file.readlines()
lineas.pop(0)
#print(lineas)
lista_dinosaurs = Lista()
lista_dino2=Lista()

for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    lista_dinosaurs.insertar(Dino(dato[0],
                                    dato[1],
                                    dato[2],
                                    dato[3],
                                    dato[4]),'time')
    lista_dino2.insertar(Dino(dato[0],
                                dato[1],
                                dato[2],
                                dato[3],
                                dato[4]), 'name')

print() 
# listado por hora
#lista_dinosaurs.barrido()

print()
# listado por monbre
#lista_dino2.barrido()

print('eliminacion zonas WYG075, SXH966 y LYF010')
dato = lista_dinosaurs.eliminar('WYG075','zone_code')
dato = lista_dino2.eliminar('WYG075','zone_code')
dato = lista_dinosaurs.eliminar('SXH966','zone_code')
dato = lista_dino2.eliminar('SXH966','zone_code')
dato = lista_dinosaurs.eliminar('LYF010','zone_code')
dato = lista_dino2.eliminar('LYF010','zone_code')

print('zona HYD195 el nombre correcto del dinosaurio es Mosasaurus.')
print()
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

#class  Dino_cola:
#    def  __init__ ( self, time, zone_code, dino_number, alert_level, name ):
#        self.time = time
#        self.zone_code = zone_code
#        self.dino_number = dino_number
#        self.alert_level = alert_level
#        self.name = name 
#
#    def  __str__ ( self ):
#        #return self.NombrePersonaje  + '-' + self . NombreHeroe + '-' + self . Genero
#        return self.time - self.zone_code - self.dino_number - self.alert_level - self.name
#
#
#
C=Cola()
Cola1=Cola()
Cola2=Cola()
#
#for Dino_cola in lista_dinosaurs:
#    dato = lista_dinosaurs
#    C.arribo(dato)
#    print(dato)

#dos colas, una con los datos de dinosaurios carnívoros y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’
while(not C.cola_vacia()):
    x=C.atencion()
    # dinosaurios carnívoros;
    if (x.type == "carnívoro" and (x.alert_level is not 'low' or x.alert_level is not 'medium')):
        Cola1.arribo(x)

    # herbívoros
    if (x.type =="herbívoro" and (x.alert_level is not 'low' or x.alert_level is not 'medium')):
        Cola2.arribo(x)

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
