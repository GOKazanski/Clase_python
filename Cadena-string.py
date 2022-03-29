texto1 = "hola mundo, soy Gabriel" # Variables
texto2 = "hola mundo"
texto3 = "SOY GABRIEL"

print (dir (texto1)) # directorio con las funciones, propiedades y métodos

# Propiedades
# '__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', # '__sizeof__', '__str__', '__subclasshook__', 

# Metodos
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

print (texto2 +', '+ texto3) # concatenar
print ("Hola, "+ texto3) # concatenar
print ("Hola, {}".format(texto3)) # concatenar
print (f"Hola, {texto3}") # concatenar
print (texto1.capitalize()) # pasa 1º letra a mayúscula
print (texto1.casefold()) # pasa todo a minúscula
print (texto1.lower()) # pasa todo a minúscula
print (texto1.title()) # pasa la 1º letra de cada palabra a mayúscula y el resto a minúscula
print (texto1.upper()) # pasa todo a mayúscula
print (texto1.swapcase()) # pasa lo que era mayúscula a minúscula y al reves
print (texto1.replace('hola', 'chau')) # remplaza un texto por otro
print (texto1.startswith('hola')) # busca si comienza con el texto seleccionado, true o false
print (texto1.endswith('EL')) # busca si termina con el texto seleccionado, true o false
print (texto1.split()) # separa la cadena por los espacios o bien por un cararter seleccionado ('G')
print (texto1.count('o')) # cuenta la cantidad de veces que se repite los caracteres iguales a la selección
print (texto1.find('G')) # Devuelve la posición donde se encuentra la cadena seleccionada, empieza de 0
print (texto1.index('s')) # Devuelve la posición donde se encuentra la cadena seleccionada, empieza de 0
print (len(texto1)) # devuelve la longitud de la cadena
print (type(texto1)) # devuelve que tipo de dato es

