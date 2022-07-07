#EJERCICIO LISTA DE LA COMPRA#

"""
lista_compra = []
producto = None
while producto != "Q":
    producto = input("Que desea comprar? ([Q] para salir)")
    if producto == 'Q':
        pass
    elif input("Seguro que quieres comprar {}? [S/N]".format(producto)) == "S":
        if producto in lista_compra:
            print("Este producto ya se encuntra en la lista")
        else:
            lista_compra.append(producto)
print("La lista de la compra es: {}".format(lista_compra))

"""


#EJERCICIO CON FOR #

"""
comas = 0
puntos = 0
espacios = 0
texto = input("introduzca el texto que quiere analizar")
caracteres = [',', '.', ' ']
for char in texto:
    if char == ',':
        comas += 1
    elif char == '.':
        puntos += 1
    elif char == ' ':
        espacios += 1

print("Las cantidad de comas:{} puntos:{} espacios:{}".format(comas,puntos,espacios))
"""

#EJERCICIO CON FOR 2#
"""

#replicar la tabla del 2#
tabla = int(input('Ingresa la tabla que deasea generar : '))
for a in range(1,11):
    if a % 2 == 0:
        print("{} x {} = {}".format(tabla,a,a*tabla))
"""

#EJERCICIO DE NUMEROS#

"""
pregunta = str(input("deseas agregar un numero a tu lista S/N: "))
numeros_de_usuario = []
while pregunta != 'N':
    numeros_de_usuario.append(int(input("Ingresa el numero que deseas: ")))
    pregunta = str(input("deseas agregar un numero a tu lista S/N: "))


numero_pequeno = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pequeno<numero:
        numero_pequeno = numero
    if numero_grande>numero:
        numero_grande = numero

print("Numero mas grande {} ".format(numero_grande))
print("Numero mas chico {}".format(numero_pequeno))
print("Numero mas Grande {}".format(max(numeros_de_usuario)))
print("Numero mas chico {}".format(min(numeros_de_usuario)))

"""

#Manera mas eficiente que la de arriba #
numeros_introducidos = input("Ingrese la lista de numeros que desea agregar separados por una coma: ")
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]

numero_pequeno = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pequeno>numero:
        numero_pequeno = numero
    if numero_grande<numero:
        numero_grande = numero

print("Numero mas grande {} ".format(numero_grande))
print("Numero mas chico {}".format(numero_pequeno))