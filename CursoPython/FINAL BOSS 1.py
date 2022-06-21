import random
cuchillo = False
print("Bienvenido a mi juego \n"
      "Escapa de la invasion alienigena")

print("Estas en tu casa descansando tranquilamente cuando de pronto,una nave espacial aterriza cerca de tu casa,\n"
      "es el comienzo de una invasion alienigena,"
      "marcianos salen de sus nave y empiezan a capturar a todos,"
      "la siguiente casa, es la tuya.\n"
      "--------------------------------------------------------------------------------------------------------------")

pregunta = input("¿Que es lo primero que haces?\n"
                 "A - Sales de tu casa en direccion contraria a los aliens\n"
                 "B - Tomas un segundo para agarrar las llaves de tu auto y sales manejando.\n"
                 "C - Te resignas, te sientas en tu sofa de nuevo a ver videos en Youtube.\n"
                 "Respuesta: ")

if pregunta == "A":
      nrandom = random.randint(1, 200)
      rcorrecta = nrandom + 90
      pregunta = int(input("Estas corriendo por las calles,viendo todo a tu alrededor hacer explosion,\n"
                       "gracias al salir lo más pronto posible ahora estas lejos de las naves,entras a una tienda,\n"
                       "quieres entrar a la seccion de armas pero esta cerrada con una puerta con contraseña,\n"
                       "pero espera, en el suelo ves un papel que dice La contraseña es 90 + {},\n"
                       "¿Cual es la contraseña?: ".format(nrandom)))
      if pregunta != rcorrecta:
          rincorrecta = pregunta
          print("MAL, como vas a creer que 90 + {} era {},obviamente era {}, por suerte,el que hizo la nota tambien creyó lo mismo que tu,\n"
                "desbloqueas la puerta y entras."
                "Esta todo vacio, solo dejaron un cuchillo, y una radio(no me preguntes que hace ahi),\n" 
                "al encenderlo escuchas:\n"
                "--Las autopistas estan bloqueadas, nuestra unica ruta de escape es la via maritima, los puertos aun estan de pie--"
                .format(nrandom, rincorrecta,rcorrecta))
          pregunta = input("Procedes a dirigirte al puerto,pero antes,¿Quieres tomar el cuchillo? (S/N): ")
          cuchillo = False


          if pregunta == "S":
            cuchillo = True
            print("Tomas el cuchillo")
          else:
              print("Bueno lo dejaras ahi")


      elif pregunta == rcorrecta:
          print("Felicidades,sabes de matematicas, desgraciadamente el que escribio la nota no, por cierto,\n"
                "los aliens llegaron detras tuya mientras hacias este calculo, has muerto...FIN")
          exit(1)


if pregunta == "B":
    pregunta = input("Casi te atrapan, pero apenas consigues escapar, las personas intentan treparse a tu auto para sobrevivir, "
                     "asi que aceleras dejandolos atras,\n ¿Que haras ahora?\n"
                     "A-Enciendes la radio,buscando algun tipo de informacion sobre zonas seguras\n"
                     "B-Te diriges a la autopista más cercana en busca de las salidas de la ciudad\n"
                     "Respuesta: ")
    if pregunta == "A":
        print("Radio:Las autopistas estan bloqueadas, nuestra unica ruta de escape es la via maritima, "
              "los puertos aun estan de pie")
        pregunta = input("Ya oiste la radio, ¿que quieres hacer?\n"
                         "A - Ir a el puerto\n"
                         "B - Ir a la autopista(Esta no)\n"
                         "Respuesta: ")
        if pregunta == "A":
            pregunta = input("Buena decision, llegas al puerto,te subes a uno de los buques de evacuacion,"
                             "entras a la cocina y ves un cuchillo, ¿Lo tomas? S/N\n"
                             "Respuesta ")
            cuchillo = False

            if pregunta == "S":
                cuchillo = True
            else:
                print("Bueno, lo dejas ahi")

        elif pregunta == "B":
            print("....Okay, estas llendo a la autopista,Oh wow, que sorpresa, autopistas totalmente bloqueadas,\n"
                  "ahora estas atrapado en el trafico,espera...¿que es eso?\n"
                  "¡Es otra nave espacial y esta llendo directo hacia ti!")
            pregunta = input("¡SAL DEL AUTO\n"
                             "A - Salir del auto\n"
                             "B - Quedarse en el auto \n"
                             "Respuesta: ")
            if pregunta == "A":
                print("Has salido a tiempo,pero la nave espacial tenia armas y eso y pues te mato,\n"
                      "Has muerto, tal vez si no hubieras ido a la autopista como decia la radio,hubieras sobrevivido\n"
                      "FIN")
                exit(1)
            elif pregunta == "B":
                print("¿Porque no saliste? Pudiste haberte salvado..o no?")
                exit(1)
    elif pregunta == "B":
        print("Oh no, autopistas totalmente bloqueadas, ahora estas atrapado en el trafico,espera...¿que es eso?\n"
              "otra nave espacial,esta llendo directo hacia ti.")
        pregunta = input("¡SAL DEL AUTO!\n"
                         "A - Salir del auto\n"
                         "B - Quedarse en el auto\n"
                         "Respuesta: ")
        if pregunta == "A":
            print("Has logrado salir,pero la nave tenia armas y eso, y pues has muerto,\n"
                  "FIN")
            exit(1)
        elif pregunta == "B":
            print("¿PORQUE NO HAS SALIDO DEL AUTO?pudiste haberte salvado...\n"
                  "FIN")
            exit(1)
if pregunta == "C":
    print("Bueno.... los marcianos llegan a tu casa, te comen, etc.\n"
          "Has muerto\n"
          "FIN")
    exit(1)



print("oh no, un mini marciano alcanza el buque,se sube a el y ataca a la gente,"
      "si tan solo tuvieras algo para defenderlos....")
if cuchillo == True:
    print("OH,claro,el Cuchillo,atacas al marciano por la espalda y salvas al barco,"
          "escapan todos hacia el horizonte,seguros,por ahora...\n" 
          "Has escapado\n"
          "FIN")
    exit(1)
else:
    print("El marciano daña el buque,todos se unden y se tiran al mar,ahi todos son "
          "comidos por una manada hambrienta de tiburones,\n"
          "tal vez esto no hubiera pasado si alguien agarraba el cuchillo cuando tuvo oportunidad\n"
          "Has muerto\n"
          "FIN")
    exit(1)