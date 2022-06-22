print("Bienvenido a escoje tu movil perfecto")

sistema_operativo = input("¿Que sistema operativo quieres que tenga tu movil?\n"
                          "A: Andrioid\n"
                          "B: iOS\n")

if sistema_operativo == "A":
    tienes_dinero = input("¿Tienes dinero?\n"
                         "A: Si\n"
                         "B: No\n")
    if tienes_dinero == "B":
        print("Tu opcion mas adequada seria un Android Chino de 100€")
        exit()
    elif tienes_dinero == "A":
        camera_movil = input("¿Te importa la camera del movil?\n"
                         "A: Si\n"
                         "B: No\n")
    if camera_movil == "A":
        print("El movil mas adequado para ti seria el Google Pixel Supercamera")
        exit()
    elif camera_movil == "B":
        print("El movil mas adequado para ti es un Android calidad-precio")
        exit()


if sistema_operativo == "B":
    tienes_dinero_2 = input("¿Tienes dinero?\n"
                         "A: Si\n"
                         "B: No\n")
    if tienes_dinero_2 == "A":
        print("Tu movil mas adequado es el iphone 13 pro max")
        exit()
    elif tienes_dinero_2 == "B":
        print("Tu movil mas adequado es un iphon de segunda mano")
        exit()


