SALIR = "SALIR"
LISTA = "LISTA"
lista_predeterminada = ["leche", "pan", "cereal", "agua"]


def crear_archivo(lista_compra):
    nombre = input("Como quieres llamar el arhcivo de la lista?: ")
    a = open(nombre + ".txt", "w")
    a.write("\n".join(lista_compra))
    a.close()

def esta_produto(lista,producto):
    if producto in lista:
        return True
    else:
        return False

def motrar_lista_predeterminada(lista):
    return print("\n".join(lista))

def pregunta_al_usuario():
    item_elegido = input("\n"+"Elije un producto para la lista [para finalizar escribe {} y {} "
                            "si quieres ver la lista de los productos que puedes agregar]: ".format(SALIR,LISTA))
    while item_elegido.lower() not in lista_predeterminada and item_elegido != SALIR and item_elegido != LISTA:
        print("Ese producto no esta disponible para colocar en la lista elije otro")
        item_elegido = input("\n" + "Elije otro producto para la lista [para finalizar escribe {} y {} "
                                    "si quieres ver la lista de los productos que puedes agregar]: ".format(SALIR,
                                                                                                            LISTA))
    return item_elegido

def main():
    lista_compra = []
    input_usuario = pregunta_al_usuario()
    while input_usuario != SALIR:
        if input_usuario == LISTA:
            motrar_lista_predeterminada(lista_predeterminada)
            input_usuario = pregunta_al_usuario()
        else:
            lista_compra.append(input_usuario)
            print("\n".join(lista_compra))
            input_usuario = pregunta_al_usuario()



    crear_archivo(lista_compra)


if __name__ == "__main__":
    main()