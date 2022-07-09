import os
import random

import readchar
#CONSTANTES#
POS_X = 0
POS_Y = 1
NUM_MAP_OBJECT = 2
WIDTH = int(input("Ingrese el ancho del tablero:"))
HIGH = int(input("Ingrese el alto del tablero: "))

#VARIABLES#
end_game = False
dead = False
tail_length = 0
tail = []
my_position = [0, 0]
map_object = []
os.system("cls")
#TABLERO#
while not end_game:
    os.system("cls")
    #Generador de comida#
    while len(map_object) < NUM_MAP_OBJECT:
        new_position = [int(random.randint(0, WIDTH-1)), int(random.randint(0, HIGH-1))]

        if new_position not in map_object and new_position != my_position:
            map_object.append(new_position)

    print("+" + "-" * (WIDTH * 3) + "+")
    for coordinate_y in range(HIGH):

        print("|", end="")

        for coordinate_x in range(WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_objects in map_object:
                if map_objects[POS_X] == coordinate_x and map_objects[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_objects

            for tail_body in tail:
                if tail_body[POS_X] == coordinate_x and tail_body[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_body

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_object.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    dead = True
                    end_game = True

            if tail_length > 10 and NUM_MAP_OBJECT !=3:
                NUM_MAP_OBJECT += 1


            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (WIDTH * 3) + "+")
    print("\n"+"Comida ingerida: {} ".format(tail_length), end="")

    #Mov#

    #direction = input("A que direccion deseas moverte? (W/A/S/D): ")

    direction = readchar.readchar().decode()

    if direction in ["w", "W"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= HIGH
    elif direction in ["a", "A"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= WIDTH
    elif direction in ["s", "S"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= HIGH
    elif direction in ["d", "D"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= WIDTH
    elif direction in ["q", "Q"]:
        end_game = True

    os.system("cls")

    if dead == True:
        print("\n")
        print("\n")
        print("\n")
        print("|-------------------------------------------------|")
        print("|------------------GAME OVER----------------------|")
        print("|--------La serpiente choco con su cola-----------|")
        print("|---------------Tu record fue {}------------------|".format(tail_length))
        print("|-------------------------------------------------|")
        print("\n")
        print("\n")
        print("\n")
    elif end_game == True:
        print("\n")
        print("|-------------------------------------------------|")
        print("|------------------NOS VEMOS----------------------|")
        print("|-------------HAS CERRADO EL JUEGO----------------|")
        print("|---------------Tu record fue {}------------------|".format(tail_length))
        print("|-------------------------------------------------|")
        print("\n")