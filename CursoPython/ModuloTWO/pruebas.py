import random
import os

#Constantes#
VIDA_PIKACHU = 80
VIDA_SQUIERTEL = 90
VIDA_LUGIA = 100
VIDA_BULBASAUR = 80
TAMANIO_BARRAS = 20

#Skills squiertel#
ATAQUE_PLACAJE = 10
ATAQUE_PISTOLA_AGUA = 12
ATAQUE_BURBUJA = 11
#Skills squiertel#
vida_squiertel_actual = VIDA_SQUIERTEL
barras_vida_squiertel = int(vida_squiertel_actual * TAMANIO_BARRAS / VIDA_SQUIERTEL)


#Skills LUGIA#
ATAQUE_AEREO = 10
ATAQUE_HIDROBOMBA = 12
ATAQUE_PREMONICION = 9
#Vida LUGIA#
vida_lugia_actual = VIDA_LUGIA
barras_vida_lugia = int(vida_lugia_actual * TAMANIO_BARRAS / VIDA_LUGIA)


#Skills pikachu#
ATAQUE_ONDA_TRUENO = 19
ATAQUE_BOLA_VOLETO = 15
ATAQUE_RAPIDO = 10
vida_pikachu_actual = VIDA_PIKACHU
barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS /VIDA_PIKACHU)


while vida_pikachu_actual > 0 and vida_lugia_actual > 0:

    print("Turno de Bulbasaur")

    ataqueS = random.randint(1, 4)
    if ataqueS == 1:
        print("Lugia ataca con Hidrobomba")
        vida_pikachu_actual -= ATAQUE_HIDROBOMBA
    elif ataqueS == 2:
        print("Lugia ataca con Premonicion")
        vida_pikachu_actual -= ATAQUE_PREMONICION
    elif ataqueS == 3:
        print("Lugia ataca con ataque aereo")
        vida_pikachu_actual -= ATAQUE_AEREO
    elif ataqueS == 4:
        print("Lugia no hizo nada")

    if vida_lugia_actual < 0:
        vida_lugia_actual = 0
    if vida_pikachu_actual < 0:
         vida_pikachu_actual = 0

    print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                            " " * (TAMANIO_BARRAS - barras_vida_pikachu), vida_pikachu_actual,
                                            VIDA_PIKACHU))

    barras_vida_lugia= int(vida_lugia_actual * TAMANIO_BARRAS / VIDA_LUGIA)
    print("Bulbasaur: [{}{}] ({}/{})".format("*" * barras_vida_lugia,
                                             " " * (TAMANIO_BARRAS - barras_vida_lugia), vida_lugia_actual,
                                              VIDA_LUGIA))

    input("Enter para continuar...\n")
    os.system("cls")
    print("Turno de Squiertel")

    ataqueS = None
    while ataqueS not in ["O", "B", "R", "N"]:
        ataqueS = input("Elegir el ataque:"+"[O]-Onda trueno "+"[B]-Bola volteo "+"[R]-Ataque rapido "+"[N]-No hacer nada: ")

        if ataqueS == "O":
            print("Pikachu ataca con onda trueno")
            vida_squiertel_actual -= ATAQUE_ONDA_TRUENO
        elif ataqueS == 'B':
            print("Pikachu ataca con bola volteo")
            vida_squiertel_actual -= ATAQUE_BOLA_VOLETO
        elif ataqueS == 'R':
            print("Pikachu hace un ataque rapido")
            vida_squiertel_actual -= ATAQUE_RAPIDO
        elif ataqueS == 'N':
            print("Pikachu no hizo nada")

        if vida_lugia_actual < 0:
            vida_lugia_actual = 0
        if vida_pikachu_actual < 0:
            vida_pikachu_actual = 0

        barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
        print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                    " " * (TAMANIO_BARRAS - barras_vida_pikachu), vida_pikachu_actual,
                                                    VIDA_PIKACHU))
        barras_vida_lugia = int(vida_lugia_actual * TAMANIO_BARRAS / VIDA_LUGIA)
        print("Bulbasaur: [{}{}] ({}/{})".format("*" * barras_vida_lugia,
                                                 " " * (TAMANIO_BARRAS - barras_vida_lugia), vida_lugia_actual,
                                                 VIDA_LUGIA))
        input("Enter para continuar...\n")
        os.system("cls")

if vida_pikachu_actual > vida_lugia_actual:
    print("Pikachu gana")
else:
    print("Bulbasaur gana")