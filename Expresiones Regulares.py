import re

texto= """Palabra de longitud 7 o mas: Persona
No finaliza con una vocal: Animal
Palabra que inicia con M segunda letra no es vocal: Mmexico - Mexico
Expresion en comillas: "Hola" "mundo"
Direcciones ip: 192.168.0.1   192.168.12.102
Horas: 10:20am    11:50pm
Telefonos: 985-100-7583   o    998-403-5664
Correo electronico: luis37.mck@gmail.com  o  luis.chankauil@itsva.edu.mx
Url: www.google.com/   o    www.facebook.com/
Codigo postal: 97740  o  98665   o  99685
"""

print()
print("Busqueda de palabras de 7 o mas letras")
print()

patron1 = r"(\w{7,})"

coincidencias1 = re.findall(patron1, texto)

for coincidencia1 in coincidencias1:
    print(coincidencia1)

print()
print("Expresiones que no finalizan con una vocal")
print()

patron2 = r"[a-zA-Záéíóú]{1,}[^aeiou\s\W]\b"

coincidencias2 = re.findall(patron2, texto)

for coincidencia2 in coincidencias2:
    print(coincidencia2)

print()
print("Las palabras que inicien con “M” donde la segunda letra no sea vocal")
print()

patron3 = r"[M][^aeiou]\w{1,}"

coincidencias3 = re.findall(patron3, texto)

for coincidencia3 in coincidencias3:
    print(coincidencia3)

print()
print("Expresiones encerradas entre comillas")
print()

patron4 = r"\"(\w{1,})\""

coincidencias4 = re.findall(patron4, texto)

for coincidencia4 in coincidencias4:
    print(coincidencia4)

print()
print("Direcciones ip's")
print()

patron5 = r"\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}"

coincidencias5 = re.findall(patron5, texto)

for coincidencia5 in coincidencias5:
    print(coincidencia5)

print()
print("Busqueda de horas")
print()

patron6 = r"\d\d\:\d\d[a|p][m]"

coincidencias6 = re.findall(patron6, texto)

for coincidencia6 in coincidencias6:
    print(coincidencia6)

print()
print("Busqueda de telefonos")
print()

patron7 = r"\d{3}-\d{3}-\d{4}"

coincidencias7 = re.findall(patron7, texto)

for coincidencia7 in coincidencias7:
    print(coincidencia7)

print()
print("Correos electronicos")
print()

patron8 = r"[a-z0-9\.-_]+@[\w\d]+\.\w"

coincidencias8 = re.findall(patron8, texto)

for coincidencia8 in coincidencias8:
    print(coincidencia8)

print()
print("Busqueda de url's")
print()

patron9 = r"\w+.[\w\-\.]+\/"

coincidencias9 = re.findall(patron9, texto)

for coincidencia9 in coincidencias9:
    print(coincidencia9)

print()
print("Busqueda de codigo postal")
print()

patron10 = r"\d{5}"

coincidencias10 = re.findall(patron10, texto)

for coincidencia10 in coincidencias10:
    print(coincidencia10)
