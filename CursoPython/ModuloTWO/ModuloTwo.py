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