SALIR = "SALIR"

def crear_archivo(lista_compra):
    nombre = input("Como quieres llamar el arhcivo de la lista?: ")
    a = open(nombre + ".txt", "w")
    a.write("\n".join(lista_compra))
    a.close()



def pregunta_al_usuario():
    return input("\n"+"Elije un producto para la lista [para finalizar escribe {}:".format(SALIR))

def guardar_en_lista_de_compra(input_usuario,lista_compra):
    if input_usuario.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya esta en la lista")
    else:
        lista_compra.append(input_usuario)
        print("\n".join(lista_compra))

def main():
    lista_compra = []
    input_usuario = pregunta_al_usuario()
    while input_usuario != SALIR:
        guardar_en_lista_de_compra(input_usuario,lista_compra)
        input_usuario = pregunta_al_usuario()
    crear_archivo(lista_compra)


if __name__ == "__main__":
    main()