import readchar

POS_X = 0
POS_Y = 1
WIDTH = int(input("Ingrese el ancho del tablero:"))
HIGH = int(input("Ingrese el alto del tablero: "))
my_position = [0,0]

while True:
    print("+" + "-" * (WIDTH * 3) + "+")
    for coordinate_y in range(HIGH):
        print("|", end="")
        for coordinate_x in range(WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-" * (WIDTH * 3) + "+")


    #Mov#

    #direction = input("A que direccion deseas moverte? (W/A/S/D): ")

    direction = readchar.readchar().decode()

    if direction == "W":
        if my_position[POS_Y] > 0:
            my_position[POS_Y] -= 1
        elif my_position[POS_Y] == 0:
            my_position[POS_Y] = HIGH
    if direction == "A":
        if my_position[POS_X] > 0:
            my_position[POS_X] -= 1
        elif my_position[POS_X] == 0:
            my_position[POS_X] = WIDTH

    if direction == "S":
        if my_position[POS_Y] < HIGH:
            my_position[POS_Y] += 1
        elif my_position[POS_Y] == HIGH:
            my_position[POS_Y] = 0
    if direction == "D":
        if my_position[POS_X] < WIDTH:
            my_position[POS_X] += 1
        elif my_position[POS_X] == WIDTH:
            my_position[POS_X] = 0

    print(my_position)