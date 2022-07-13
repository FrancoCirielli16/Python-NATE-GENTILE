import os
import random
#POKEMONS#

#Constantes#
VIDA_PIKACHU = 80
VIDA_SQUIERTEL = 90
VIDA_BULBASAUR = 80
VIDA_LUGIA = 100
TAMANIO_BARRAS = 20

#Skills LUGIA#
ATAQUE_AEREO = 10
ATAQUE_HIDROBOMBA = 12
ATAQUE_PREMONICION = 9
#Vida LUGIA#
vida_lugia_actual = VIDA_LUGIA
barras_vida_squiertel = int(vida_lugia_actual * TAMANIO_BARRAS / VIDA_LUGIA)


#Skills bulbasaur#
ATAQUE_PLACAJE_TACKLE = 10
ATAQUE_GRUÑIDO = 12
ATAQUE_DRENADORA = 11
#Vida bulbasaur#
vida_bulbasaur_actual = VIDA_BULBASAUR
barras_vida_squiertel = int(vida_bulbasaur_actual * TAMANIO_BARRAS / VIDA_BULBASAUR)


#Skills squiertel#
ATAQUE_PLACAJE = 10
ATAQUE_PISTOLA_AGUA = 12
ATAQUE_BURBUJA = 11
#Skills squiertel#
vida_squiertel_actual = VIDA_SQUIERTEL
barras_vida_squiertel = int(vida_squiertel_actual * TAMANIO_BARRAS / VIDA_SQUIERTEL)

#Skills pikachu#
ATAQUE_ONDA_TRUENO = 19
ATAQUE_BOLA_VOLETO = 15
ATAQUE_RAPIDO = 10
vida_pikachu_actual = VIDA_PIKACHU
barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS /VIDA_PIKACHU)



#MAPAS#


import readchar

#CONSTANTES#
POS_X = 0
POS_Y = 1
NUM_MAP_OBJECT = 3


#MAPA OBSTACULOS#
obstacle_definition= '''\
#####     #####################################
#####     #####################################
#####     ###########                     #####
#####     ###########                     #####
#####          ######                     #####
#####          ######        #####        #####
#####                        #####        #####
#####                        #####        #####
############                 #####        #####
########################                  #####
########################                  #####
########################             ##########
########################             ##########
########################             ##########
##############################       ##########
##############################                #
######                                        #
######                                        #
######                                        #
###############################################\
'''
#GENERADOR DE LISTA#
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
#TAMAÑO#
WIDTH = len(obstacle_definition[0])
HIGH = len(obstacle_definition)


#VARIABLES#
perdio = 0
end_game = False
end_game2 = False
dead = False
my_position = [7, 0]
map_object = []
wins = 0

#Generador de enemigos#
while len(map_object) < NUM_MAP_OBJECT:
    food = [int(random.randint(0, WIDTH-1)), int(random.randint(0, HIGH-1))]
    if food not in map_object and food != my_position and obstacle_definition[food[POS_Y]][food[POS_X]] != "#":
        map_object.append(food)

os.system("cls")
#TABLERO#
while not end_game:
    os.system("cls")
    print("+" + "-" * (WIDTH * 2) + "+")
    for coordinate_y in range(HIGH):

        print("|", end="")

        for coordinate_x in range(WIDTH):

            char_to_draw = "  "
            object_in_cell = None

            for map_objects in map_object:
                if map_objects[POS_X] == coordinate_x and map_objects[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_objects

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                if object_in_cell:
                    pokemon_figth = random.randint(0, 2)
                    vida_pikachu_actual = VIDA_PIKACHU
                    if pokemon_figth == 0 and vida_squiertel_actual != 0:
                        os.system("cls")
                        while vida_pikachu_actual > 0 and vida_squiertel_actual > 0:
                            print("\n"+"Parece que tienes que luchas contra Squirtel")
                            print("Turno de Squirtel")

                            ataqueS = random.randint(1, 4)
                            if ataqueS == 1:
                                print("Squirtel ataca con placaje")
                                vida_pikachu_actual -= ATAQUE_PLACAJE
                            elif ataqueS == 2:
                                print("Squirtel ataca con burbuja")
                                vida_pikachu_actual -= ATAQUE_BURBUJA
                            elif ataqueS == 3:
                                print("Squirtel ataca con pistola de agua")
                                vida_pikachu_actual -= ATAQUE_PISTOLA_AGUA
                            elif ataqueS == 4:
                                print("Squirtel no hizo nada")

                            if vida_squiertel_actual < 0:
                                vida_squiertel_actual = 0
                            if vida_pikachu_actual < 0:
                                vida_pikachu_actual = 0

                            barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
                            print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                                    " " * (TAMANIO_BARRAS - barras_vida_pikachu),
                                                                    vida_pikachu_actual,
                                                                    VIDA_PIKACHU))

                            barras_vida_squiertel = int(vida_squiertel_actual * TAMANIO_BARRAS / VIDA_SQUIERTEL)
                            print("Squirtel: [{}{}] ({}/{})".format("*" * barras_vida_squiertel,
                                                                    " " * (TAMANIO_BARRAS - barras_vida_squiertel),
                                                                    vida_squiertel_actual,
                                                                    VIDA_SQUIERTEL))

                            input("Enter para continuar...\n")
                            os.system("cls")
                            print("Turno de Pikachu")

                            ataqueP = None
                            while ataqueP not in ["O", "B", "R", "N"]:
                                ataqueP = input(
                                    "Elegir el ataque:" + "[O]-Onda trueno " + "[B]-Bola volteo " + "[R]-Ataque rapido " + "[N]-No hacer nada: ")

                                if ataqueP == "O":
                                    print("Pikachu ataca con onda trueno")
                                    vida_squiertel_actual -= ATAQUE_ONDA_TRUENO
                                elif ataqueP == 'B':
                                    print("Pikachu ataca con bola volteo")
                                    vida_squiertel_actual -= ATAQUE_BOLA_VOLETO
                                elif ataqueP == 'R':
                                    print("Pikachu hace un ataque rapido")
                                    vida_squiertel_actual -= ATAQUE_RAPIDO
                                elif ataqueP == 'N':
                                    print("Pikachu no hizo nada")

                                if vida_squiertel_actual < 0:
                                    vida_squiertel_actual = 0
                                if vida_pikachu_actual < 0:
                                    vida_pikachu_actual = 0

                                barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
                                print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                                        " " * (TAMANIO_BARRAS - barras_vida_pikachu),
                                                                        vida_pikachu_actual,
                                                                        VIDA_PIKACHU))
                                print("Squirtel: [{}{}] ({}/{})".format("*" * barras_vida_squiertel,
                                                                        " " * (TAMANIO_BARRAS - barras_vida_squiertel),
                                                                        vida_squiertel_actual,
                                                                        VIDA_SQUIERTEL))
                                input("Enter para continuar...\n")
                                os.system("cls")

                        if vida_pikachu_actual > vida_squiertel_actual:
                            print("Pikachu gana")
                            map_object.remove(object_in_cell)
                            wins += 1
                        else:
                            print("Squirtel gana")
                            perdio += 1
                            if perdio == 3:
                                dead = True
                                end_game = True
                    else:
                        if pokemon_figth == 1 and vida_bulbasaur_actual != 0:
                            os.system("cls")
                            while vida_pikachu_actual > 0 and vida_bulbasaur_actual > 0:
                                print("\n"+"Parece que tienes que luchas contra Bulbasaur")
                                print("Turno de Bulbasaur")

                                ataqueB = random.randint(1, 4)
                                if ataqueB == 1:
                                    print("Bulbasaur ataca con Placaje")
                                    vida_pikachu_actual -= ATAQUE_PLACAJE_TACKLE
                                elif ataqueB == 2:
                                    print("Bulbasaur ataca con Gruñido")
                                    vida_pikachu_actual -= ATAQUE_GRUÑIDO
                                elif ataqueB == 3:
                                    print("Bulbasaur ataca con Drenadora")
                                    vida_pikachu_actual -= ATAQUE_DRENADORA
                                elif ataqueB == 4:
                                    print("Bulbasaur no hizo nada")

                                if vida_bulbasaur_actual < 0:
                                    vida_bulbasaur_actual = 0
                                if vida_pikachu_actual < 0:
                                    vida_pikachu_actual = 0

                                barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
                                print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                                        " " * (TAMANIO_BARRAS - barras_vida_pikachu),
                                                                        vida_pikachu_actual,
                                                                        VIDA_PIKACHU))

                                barras_vida_bulbasaur = int(vida_bulbasaur_actual * TAMANIO_BARRAS / VIDA_BULBASAUR)
                                print("Bulbasaur: [{}{}] ({}/{})".format("*" * barras_vida_bulbasaur,
                                                                         " " * (TAMANIO_BARRAS - barras_vida_bulbasaur),
                                                                         vida_bulbasaur_actual,
                                                                         VIDA_BULBASAUR))

                                input("Enter para continuar...\n")
                                os.system("cls")
                                print("Turno de Pikachu")

                                ataqueP = None
                                while ataqueP not in ["O", "B", "R", "N"]:
                                    ataqueP = input(
                                        "Elegir el ataque:" + "[O]-Onda trueno " + "[B]-Bola volteo " + "[R]-Ataque rapido " + "[N]-No hacer nada: ")

                                    if ataqueP == "O":
                                        print("Pikachu ataca con onda trueno")
                                        vida_bulbasaur_actual -= ATAQUE_ONDA_TRUENO
                                    elif ataqueP == 'B':
                                        print("Pikachu ataca con bola volteo")
                                        vida_bulbasaur_actual -= ATAQUE_BOLA_VOLETO
                                    elif ataqueP == 'R':
                                        print("Pikachu hace un ataque rapido")
                                        vida_bulbasaur_actual -= ATAQUE_RAPIDO
                                    elif ataqueP == 'N':
                                        print("Pikachu no hizo nada")

                                    if vida_bulbasaur_actual < 0:
                                        vida_bulbasaur_actual = 0
                                    if vida_pikachu_actual < 0:
                                        vida_pikachu_actual = 0

                                    barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
                                    print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                                            " " * (TAMANIO_BARRAS - barras_vida_pikachu),
                                                                            vida_pikachu_actual,
                                                                            VIDA_PIKACHU))
                                    barras_vida_bulbasaur = int(vida_bulbasaur_actual * TAMANIO_BARRAS / VIDA_BULBASAUR)
                                    print("Bulbasaur: [{}{}] ({}/{})".format("*" * barras_vida_bulbasaur,
                                                                             " " * (TAMANIO_BARRAS - barras_vida_bulbasaur),
                                                                             vida_bulbasaur_actual,
                                                                             VIDA_BULBASAUR))
                                    input("Enter para continuar...\n")
                                    os.system("cls")

                            if vida_pikachu_actual > vida_bulbasaur_actual:
                                print("Pikachu gana")
                                map_object.remove(object_in_cell)
                                wins += 1
                            else:
                                print("Bulbasaur gana")
                                perdio += 1
                                if perdio == 3:
                                    dead = True
                                    end_game = True
                        else:
                            if pokemon_figth == 2 and vida_lugia_actual != 0:
                                os.system("cls")
                                while vida_pikachu_actual > 0 and vida_lugia_actual > 0:
                                    print("\n"+"Parece que tienes que luchas contra Lugia")
                                    print("Turno de lugia")

                                    ataqueL = random.randint(1, 4)
                                    if ataqueL == 1:
                                        print("Lugia ataca con Hidrobomba")
                                        vida_pikachu_actual -= ATAQUE_HIDROBOMBA
                                    elif ataqueL == 2:
                                        print("Lugia ataca con Premonicion")
                                        vida_pikachu_actual -= ATAQUE_PREMONICION
                                    elif ataqueL == 3:
                                        print("Lugia ataca con ataque aereo")
                                        vida_pikachu_actual -= ATAQUE_AEREO
                                    elif ataqueL == 4:
                                        print("Lugia no hizo nada")

                                    if vida_lugia_actual < 0:
                                        vida_lugia_actual = 0
                                    if vida_pikachu_actual < 0:
                                        vida_pikachu_actual = 0

                                    barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
                                    print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                                            " " * (TAMANIO_BARRAS - barras_vida_pikachu),
                                                                            vida_pikachu_actual,
                                                                            VIDA_PIKACHU))

                                    barras_vida_lugia = int(vida_lugia_actual * TAMANIO_BARRAS / VIDA_LUGIA)
                                    print("Lugia: [{}{}] ({}/{})".format("*" * barras_vida_lugia,
                                                                             " " * (TAMANIO_BARRAS - barras_vida_lugia),
                                                                             vida_lugia_actual,
                                                                             VIDA_LUGIA))

                                    input("Enter para continuar...\n")
                                    os.system("cls")
                                    print("Turno de Pikachu")

                                    ataqueP = None
                                    while ataqueP not in ["O", "B", "R", "N"]:
                                        ataqueP = input(
                                            "Elegir el ataque:" + "[O]-Onda trueno " + "[B]-Bola volteo " + "[R]-Ataque rapido " + "[N]-No hacer nada: ")

                                        if ataqueP == "O":
                                            print("Pikachu ataca con onda trueno")
                                            vida_lugia_actual -= ATAQUE_ONDA_TRUENO
                                        elif ataqueP == 'B':
                                            print("Pikachu ataca con bola volteo")
                                            vida_lugia_actual -= ATAQUE_BOLA_VOLETO
                                        elif ataqueP == 'R':
                                            print("Pikachu hace un ataque rapido")
                                            vida_lugia_actual -= ATAQUE_RAPIDO
                                        elif ataqueP == 'N':
                                            print("Pikachu no hizo nada")

                                        if vida_lugia_actual < 0:
                                            vida_lugia_actual = 0
                                        if vida_pikachu_actual < 0:
                                            vida_pikachu_actual = 0

                                        barras_vida_pikachu = int(vida_pikachu_actual * TAMANIO_BARRAS / VIDA_PIKACHU)
                                        print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                                                                " " * (TAMANIO_BARRAS - barras_vida_pikachu),
                                                                                vida_pikachu_actual,
                                                                                VIDA_PIKACHU))
                                        barras_vida_lugia = int(vida_lugia_actual * TAMANIO_BARRAS / VIDA_LUGIA)
                                        print("Lugia: [{}{}] ({}/{})".format("*" * barras_vida_lugia,
                                                                                 " " * (TAMANIO_BARRAS - barras_vida_lugia),
                                                                                 vida_lugia_actual,
                                                                                 VIDA_LUGIA))
                                        input("Enter para continuar...\n")
                                        os.system("cls")

                                if vida_pikachu_actual > vida_lugia_actual:
                                    print("Pikachu gana")
                                    map_object.remove(object_in_cell)
                                    wins += 1
                                else:
                                    print("Lugia gana")
                                    perdio += 1
                                    if perdio > 3:
                                        dead = True
                                        end_game = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            if wins == NUM_MAP_OBJECT:
                end_game2 = True


            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (WIDTH * 2) + "+")
    print("\n" + "Veces perdidas: {} (No pierdas mas de 3 veces".format(perdio), end="")
    #Mov#

    direction = readchar.readchar().decode()
    new_position = None
    if direction in ["w", "W"]:
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % HIGH]

    elif direction in ["a", "A"]:
        new_position = [(my_position[POS_X] - 1) % WIDTH, my_position[POS_Y]]

    elif direction in ["s", "S"]:
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % HIGH]

    elif direction in ["d", "D"]:
        new_position = [(my_position[POS_X] + 1) % WIDTH, my_position[POS_Y]]

    elif direction in ["q", "Q"]:
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")

    if dead == True:
        print("\n")
        print("\n")
        print("\n")
        print("|-------------------------------------------------|")
        print("|------------------GAME OVER----------------------|")
        print("|-----Has perdido con tu pokemon 3 veces----------|")
        print("|--------Derrotaste a {} entrenadores-------------|".format(wins))
        print("|-------------------------------------------------|")
        print("\n")
        print("\n")
        print("\n")
    elif end_game == True:
        print("\n")
        print("|-------------------------------------------------|")
        print("|------------------NOS VEMOS----------------------|")
        print("|-------------HAS CERRADO EL JUEGO----------------|")
        print("|---------------Tu record fue {}------------------|".format(wins))
        print("|-------------------------------------------------|")
        print("\n")
    elif end_game2 == True:
        print("\n")
        print("|------------------------------------------------------------|")
        print("|-----------------------Has GANADO---------------------------|")
        print("|-----Pudiste ganarle a todos los entrenadores pokemons------|")
        print("|------------------------------------------------------------|")
        print("\n")