#EJERCICIO LISTA DE LA COMPRA#

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

