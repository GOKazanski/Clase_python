from jurassic_park import dinosaurs
from Parcial_Lista import Lista
from Parcial_Cola import Cola

class Dino:
    def __init__(self, time, zone_code, dino_number, alert_level, name):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        self.name = name     
    
    def __str__(self):
        return f"{self.time} - {self.zone_code} - {self.dino_number} - {self.alert_level} - {self.name}"

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
                                    dato[4]), 'time')
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



#dos colas, una con los datos de dinosaurios carnívoros y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’

c=Cola()
cola1=Cola()
cola2=Cola()
cant_dino=lista_dinosaurs.tamanio()

for i in range(cant_dino):
    dato = lista_dinosaurs.time
    c.arribo(dato)
    print(dato)
