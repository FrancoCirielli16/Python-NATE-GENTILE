import random
#Skills squiertel#
vida_squiertel = 90
vida_squiertel_actual = vida_squiertel
barras_vida_squiertel = int(vida_squiertel_actual * 10 / vida_squiertel)
ataque_placaje = 10
ataque_pistola_agua = 12
ataque_burbuja = 9
#Skills pikachu#
vida_pikachu = 80
vida_pikachu_actual = vida_pikachu
barras_vida_pikachu = int(vida_pikachu_actual * 10 /vida_pikachu)
ataque_onda_trueno = 11
ataque_bola_volteo = 10

while vida_pikachu_actual > 0 and vida_squiertel_actual > 0:
    print("Pikachu:  [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                        " " * (10 - barras_vida_pikachu),vida_pikachu_actual,vida_pikachu))
    print("Squirtel: [{}{}] ({}/{})".format("*" * barras_vida_squiertel,
                                        " " * (10 - barras_vida_squiertel),vida_squiertel_actual,vida_squiertel))
    print("Turno de Pikachu")
    print("---------------------------------------------------------------------------------------")
    ataqueP = random.randint(1, 2)
    if (ataqueP == 1):
        print("Pikachu ataca con bola volteo")
        vida_squiertel_actual -= ataque_bola_volteo
        barras_vida_squiertel = int(vida_squiertel_actual * 10 / vida_squiertel)
        print("Squirtel: [{}{}] ({}/{})".format("*" * barras_vida_squiertel,
                                        " " * (10 - barras_vida_squiertel),vida_squiertel_actual,vida_squiertel))
    else:
        print("Pikachu ataca con onda trueno")
        vida_squiertel_actual -= ataque_bola_volteo
        barras_vida_squiertel = int(vida_squiertel_actual * 10 / vida_squiertel)
        print("Squirtel: [{}{}] ({}/{})".format("*" * barras_vida_squiertel,
                                        " " * (10 - barras_vida_squiertel),vida_squiertel_actual,vida_squiertel))
    print("Turno de Squiertel")
    print("---------------------------------------------------------------------------------------")
    ataqueS = None
    while ataqueS != "P" and ataqueS != "B" and ataqueS != "A":
        ataqueS = input("Elegir el ataque:"+
                                            "\n"+"[P]-Placaje"+
                                            "\n"+"[B]-Burbuja"+
                                            "\n"+"[A]-Pistola de agua"+"\n")
        if ataqueS == "P":
            print("Squirtel ataca con placaje")
            vida_pikachu_actual -= ataque_placaje
            barras_vida_pikachu = int(vida_pikachu_actual * 10 /vida_pikachu)
            print("La vida de pikachu bajo [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                            " " * (10 - barras_vida_pikachu),vida_pikachu_actual,vida_pikachu))
        else:
            if ataqueS == "B":
                print("Squirtel ataca con burbuja")
                vida_pikachu_actual -= ataque_burbuja
                barras_vida_pikachu = int(vida_pikachu_actual * 10 /vida_pikachu)
                print("La vida de pikachu bajo [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                            " " * (10 - barras_vida_pikachu),vida_pikachu_actual,vida_pikachu))
            else:
                if ataqueS == "A":
                    print("Squirtel ataca con pistola de agua")
                    vida_pikachu_actual -= ataque_pistola_agua
                    barras_vida_pikachu = int(vida_pikachu_actual * 10 /vida_pikachu)
                    print("La vida de pikachu bajo [{}{}] ({}/{})".format("*" * barras_vida_pikachu,
                                            " " * (10 - barras_vida_pikachu),vida_pikachu_actual,vida_pikachu))
    print("---------------------------------------------------------------------------------------")

if vida_pikachu > vida_squiertel:
    print("Pikachu gana")
else:
    print("Squirtel gana")