print("\nbienvenido al test de el lolero" + "\n")
# valor para cada pregunta
puntuacion = 0

# por pregunta
puntuacion_maxima = 15
# el intermedio es valido.
puntuacion_minima = 0

# pregunta1


respuesta = int(input("por cual linea es mas facil llega al nexo enemigo: ?\n"

                      "\n[1] = por top" + "\n"
                                          "\n[2] = por mid" + "\n"
                                                              "\n[3] = por bot" + "\n"))

if respuesta == 1:
    puntuacion += 0
    print("perfecto!")

elif respuesta == 2:
    puntuacion += 15
    print("perfecto!")

elif respuesta == 3:
    puntuacion += 0
    print("perfecto!")

else:
    print("elige una opcion valida.")
    exit(1)
    # pregunta 2

respuesta = int(input("si en tu equipo deben decidir entre sacar baron o sacar dragon ancestral, cual escogerias: ?\n"
                      "\n[1] = dragon" + "\n"
                                         "\n[2] = baron" + "\n"))
if respuesta == 1:
    puntuacion += 15
elif respuesta == 2:
    puntuacion += 5
else:
    print("responde un numero valido")
    exit(1)

    # pregunta 3

respuesta = int(input("si tu support rota a alguna linea, que debes hacer como adc?: ?\n"
                      "\n[1] = pushear como un loco hasta la torre" + "\n"
                                                                      "\n[2] = esperar bajo torre aunque se tarde 1 hora en volver" + "\n"
                                                                                                                                      "\n[3] = esperar lo mas cerca de mi torre jugando defensivo" + "\n"
                                                                                                                                                                                                     "\n[4] = lo puteo en el chat :)"))
if respuesta == 1:
    puntuacion += 5
    print("perfecto!")

elif respuesta == 2:
    puntuacion += 5
    print("perfecto")

elif respuesta == 3:
    puntuacion += 15
    print("perfecto")

elif respuesta == 4:
    puntuacion += 0
    print("vaya!")

else:
    print("elige una opcion valida")
    exit(1)

    # pregunta 4

respuesta = int(input("contra un enemigo que tiene 150 de armadura, que deberiamos armarnos?: ?\n"
                      "\n[1] = un objeto que aumente su daño dependiendo de la vida del objetivo" + "\n"
                                                                                                    "\n[2] = un objeto que tenga letalidad" + "\n"
                                                                                                                                              "\n[3] = un objeto que tenga penetracion de armadura" + "\n"
                                                                                                                                                                                                      "\n[4] = lo puteo en el chat :)"))

if respuesta == 1:
    puntuacion += 1
    print("perfecto")

elif respuesta == 2:
    puntuacion += 5
    print("perfecto")

elif respuesta == 3:
    puntuacion += 15
    print("perfecto")

elif respuesta == 4:
    puntuacion += 0
    print("vaya!")

else:
    print("elige una opcion valida")
    exit(1)

    # pregunta 5

respuesta = int(input("si hay un aliado que esta generando toxicidad en el chat (insultando), que debo hacer?: ?\n"
                      "\n[1] = entablo una conversacion formal con el pidiendole que porfavor se calme" + "\n"
                                                                                                          "\n[2] = lo ignoro y sigo adelante con mi juego" + "\n"
                                                                                                                                                             "\n[3] = lo muteo y sigo adelante con mi juego" + "\n"
                                                                                                                                                                                                               "\n[4] = le respondo de la misma manera en el chat ignorando mi partida"))

if respuesta == 1:
    puntuacion += 10
    print("perfecto")

elif respuesta == 2:
    puntuacion += 10
    print("perfecto")

elif respuesta == 3:
    puntuacion += 15
    print("perfecto")

elif respuesta == 4:
    puntuacion += 1
    print("vaya!")

else:
    print("elige una opcion valida")
    exit(1)

    # resultado final

if puntuacion >= 0 and puntuacion <= 5:
    print("tu puntuacion fue {}/75".format(puntuacion))
    print("\nvaya novato...")

elif puntuacion >= 6 and puntuacion <= 25:
    print("tu puntuacion fue {}/75".format(puntuacion))
    print("\nya veo porque estas en bronce, fuera de aqui!")


elif puntuacion >= 26 and puntuacion <= 40:
    print("tu puntuacion fue {}/75".format(puntuacion))
    print("\nbueno, no esta mal :)")

elif puntuacion >= 41 and puntuacion <= 50:
    print("tu puntuacion fue {}/75".format(puntuacion))
    print("\nde seguro eres oro/platino!")

elif puntuacion >= 51 and puntuacion <= 75:
    print("tu puntuacion fue {}/75".format(puntuacion))
    print("\nmenudo dios, pasame el whatsapp de faker.")

    # ------------FIN---------