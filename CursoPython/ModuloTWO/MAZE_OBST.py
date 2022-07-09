import os
import random

import readchar
#CONSTANTES#
POS_X = 0
POS_Y = 1
NUM_MAP_OBJECT = 5


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
end_game = False
dead = False
tail_length = 0
tail = []
my_position = [7, 0]
map_object = []

os.system("cls")

#TABLERO#
while not end_game:
    os.system("cls")
    #Generador de comida#
    while len(map_object) < NUM_MAP_OBJECT:
        food = [int(random.randint(0, WIDTH-1)), int(random.randint(0, HIGH-1))]

        if food not in map_object and food != my_position and obstacle_definition[food[POS_Y]][food[POS_X]] != "#":
            map_object.append(food)

    print("+" + "-" * (WIDTH * 2) + "+")
    for coordinate_y in range(HIGH):

        print("|", end="")

        for coordinate_x in range(WIDTH):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_objects in map_object:
                if map_objects[POS_X] == coordinate_x and map_objects[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_objects

            for tail_body in tail:
                if tail_body[POS_X] == coordinate_x and tail_body[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_body

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                if object_in_cell:
                    map_object.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    dead = True
                    end_game = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"



            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (WIDTH * 2) + "+")
    print("\n"+"Comida ingerida: {} ".format(tail_length), end="")

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
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

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