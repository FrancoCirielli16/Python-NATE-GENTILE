import random
import os

#Constantes#
VIDA_PIKACHU = 80
VIDA_SQUIERTEL = 90
TAMANIO_BARRAS = 20

#Skills squiertel#
ATAQUE_PLACAJE = 10
ATAQUE_PISTOLA_AGUA = 12
ATAQUE_BURBUJA = 11
#Skills squiertel#
vida_squiertel_actual = VIDA_SQUIERTEL
barras_vida_squiertel = int(vida_squiertel_actual * TAMANIO_BARRAS / VIDA_SQUIERTEL)

#Skills pikachu#
ATAQUE_ONDA_TRUENO = 11
ATAQUE_BOLA_VOLETO = 10
vida_pikachu_actual = VIDA_PIKACHU
barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS /VIDA_PIKACHU)


while vida_pikachu_actual > 0 and vida_squiertel_actual > 0:

    print("Turno de Pikachu")

    ataqueP = random.randint(1, 2)
    if (ataqueP == 1):
        print("Pikachu ataca con bola volteo")
        vida_squiertel_actual -= ATAQUE_BOLA_VOLETO
    else:
        print("Pikachu ataca con onda trueno")
        vida_squiertel_actual -= ATAQUE_ONDA_TRUENO

    if vida_squiertel_actual < 0:
        vida_squiertel_actual = 0
    if vida_pikachu_actual < 0:
         vida_pikachu_actual = 0

    print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                            " " * (TAMANIO_BARRAS - barras_vida_pikachu), vida_pikachu_actual,
                                            VIDA_PIKACHU))

    barras_vida_squiertel = int(vida_squiertel_actual * TAMANIO_BARRAS / VIDA_SQUIERTEL)
    print("Squirtel: [{}{}] ({}/{})".format("*" * barras_vida_squiertel,
                                             " " * (TAMANIO_BARRAS - barras_vida_squiertel), vida_squiertel_actual,
                                               VIDA_SQUIERTEL))

    input("Enter para continuar...\n")
    os.system("cls")
    print("Turno de Squiertel")

    ataqueS = None
    while ataqueS != "P" and ataqueS != "B" and ataqueS != "A":
        ataqueS = input("Elegir el ataque:"+"[P]-Placaje "+"[B]-Burbuja "+"[A]-Pistola de agua "+"[N]-No hacer nada: ")

        if ataqueS == "P":
            print("Squirtel ataca con placaje")
            vida_pikachu_actual -= ATAQUE_PLACAJE
        elif ataqueS == 'B':
            print("Squirtel ataca con burbuja")
            vida_pikachu_actual -= ATAQUE_BURBUJA
        elif ataqueS == 'A':
            print("Squirtel ataca con pistola de agua")
            vida_pikachu_actual -= ATAQUE_PISTOLA_AGUA
        elif ataqueS == 'N':
            print("Squirtel no hizo nada")

        if vida_squiertel_actual < 0:
            vida_squiertel_actual = 0
        if vida_pikachu_actual < 0:
            vida_pikachu_actual = 0

        barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
        print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                    " " * (TAMANIO_BARRAS - barras_vida_pikachu), vida_pikachu_actual,
                                                    VIDA_PIKACHU))
        print("Squirtel: [{}{}] ({}/{})".format("*" * barras_vida_squiertel,
                                                " " * (TAMANIO_BARRAS - barras_vida_squiertel), vida_squiertel_actual,
                                                VIDA_SQUIERTEL))
        input("Enter para continuar...\n")
        os.system("cls")

if vida_pikachu_actual > vida_squiertel_actual:
    print("Pikachu gana")
else:
    print("Squirtel gana")