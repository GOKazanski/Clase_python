from Parcial_Lista import Lista

class Dino:
    def __init__(self, nombre, tipo_dino, numero, periodo, explorador):
        self.nombre = nombre
        self.tipo_dino = tipo_dino
        self.numero = numero
        self.periodo = periodo
        self.explorador = explorador
    
    def __str__(self):
        return f"{self.nombre} - {self.tipo_dino} - {self.numero} - {self.periodo} - {self.explorador}"

dinosaurs = [
    {'name': 'Tyrannosaurus Rex', 'type': 'carnívoro ', 'number': 8,'period': 'cretácico superior', 'named_by': 'Osborn, 1905'},
    {'name': 'Mosasaurus', 'type': 'carnívoro ', 'number': 11,'period': 'cretácico superior', 'named_by': 'Mantell, 1829'},
    {'name': 'Carnotaurus', 'type': 'carnívoro ', 'number': 14,'period': 'cretácico superior', 'named_by': 'Bonaparte, 1985'},
    {'name': 'Raptors (Dromaeosauridae)', 'type': 'carnívoro ', 'number': 4,'period': 'cretácico', 'named_by': 'Matthew & Brown, 1922'},
    {'name': 'Pteranodon', 'type': 'carnívoro ', 'number': 6,'period': 'cretácico superior', 'named_by': 'Marsh, 1876'},
    {'name': 'Compsognathus', 'type': 'carnívoro ', 'number': 2, 'period': 'jurásico superior', 'named_by': 'Wagner, 1859'},
    {'name': 'Giganotosaurus', 'type': 'carnívoro ', 'number': 16, 'period': 'cretácico superior', 'named_by': 'Coria & Salgado, 1995'},
    {'name': 'Allosaurus', 'type': 'carnívoro ', 'number': 15, 'period': 'jurásico superior', 'named_by': 'Marsh, 1877'},
    {'name': 'Spinosaurus', 'type': 'carnívoro ', 'number': 13, 'period': 'cretácico superior', 'named_by': 'Stromer, 1915'},
    {'name': 'Dilophosaurus', 'type': 'carnívoro ', 'number': 3, 'period': 'jurásico inferior', 'named_by': 'Welles, 1954'},
    {'name': 'Triceratops', 'type': 'herbívoro ', 'number': 10, 'period': 'cretácico superior', 'named_by': 'Marsh, 1889'},
    {'name': 'Brachiosaurus', 'type': 'herbívoro ', 'number': 12, 'period': 'jurásico superior', 'named_by': 'Riggs, 1903'},
    {'name': 'Diplodocus', 'type': 'herbívoro ', 'number': 7, 'period': 'jurásico superior', 'named_by': 'Marsh, 1878'},
    {'name': 'Stegosaurus', 'type': 'herbívoro ', 'number': 5, 'period': 'jurásico superior', 'named_by': 'Marsh, 1887'},
    {'name': 'Parasaurolophus', 'type': 'herbívoro ', 'number': 9, 'period': 'cretácico superior', 'named_by': 'Parks, 1922'},
    {'name': 'Ankylosaurus', 'type': 'herbívoro ', 'number': 1, 'period': 'cretácico superior', 'named_by': 'Brown, 1908'},
    {'name': 'Pachycephalosaurus', 'type': 'herbívoro ', 'number': 17, 'period': 'cretácico superior', 'named_by': 'Brown & Schlaikjer, 1943'},
]

lista_dinosaurs = Lista()

for dino in dinosaurs:
    lista_dinosaurs.insertar(Dino(dino['name'],
                                    dino['type'],
                                    dino['number'],
                                    dino['period'],
                                    dino['named_by']), 'nombre')

print() 
#lista_dinosaurs.barrido()



#determinar cual de nuestro dinosaurios fuel el ultimo en ser descubierto y quien lo hizo. 








#class Error:
#    
#    def __init__(self, tiempo, zona, n_dino, alerta):
#        self.tiempo = tiempo
#        self.zona = zona
#        self.n_dino = n_dino
#        self.alerta = alerta
#
#    def __str__(self):
#        return f"{self.tiempo} | {self.zona} | {self.n_dino} | {self.alerta}"
#
#file = open('/home/gabriel/Documentos/2° año/Algoritmos/Clase_python/Parciales/alerts.txt')
#lineas = file.readlines()
#
#lista_error=Lista()
#
#lista = []
#
#lineas.pop(0)  # quitar cabecera
#for linea in lineas:
#    datos = linea.split(';')
#    datos.pop(-1)#time;zone_code;dino_number;alert_level
#    lista_error.insertar(Error(datos ['time'],
#                                datos['zone_code'],
#                                datos['dino_number'],
#                                datos['alert_level']),
#                            campo='tiempo')
#                    
#lista_error.barrido