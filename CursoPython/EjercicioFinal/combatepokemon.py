import random
from pprint import pprint

from CursoPython.EjercicioFinal.Pokeload import get_all_pokemons


def get_player_profile(pokemon_list):
    return {"player_name": input("¿Cual es tu nombre?: "),
            "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
            "combats": 0,
            "pokeballs": 0,
            "health_potion": 0,
            }


def any_player_pokemon_lives(profile):
    return sum([pokemon["current_health"] for pokemon in profile["pokemon_inventory"]]) > 0


def choose_pokemon(profile):
    choseen = None
    while not choseen:
        for index in range(len(profile["pokemon_inventory"])):
            print("{} - {}".format(index, pokemon_info(profile["pokemon_inventory"][index])))
        try:
            return profile["pokemon_inventory"][int(input("¿Cual elejis?: "))]
        except (ValueError, IndexError):
            print("Opcion invalida!!, volve a intentarlo")


def pokemon_info(pokemon):
    return "{} | lvl {} | tipo {}| HP {}/{}".format(pokemon["name"],
                                                    pokemon["level"],
                                                    pokemon["type"],
                                                    pokemon["current_health"],
                                                    pokemon["base_health"])


def player_attack(my_pokemon,enemy):
    #implementar multiplicadores dependiendo el tipo de pokemon
    """ Normal: débil frente a Lucha
        Fuego: débil frente a Agua, Tierra, Roca
        Agua: débil frente a Planta, Eléctrico
        Planta: débil frente a Fuego, Hielo, Veneno, Volador, Bicho
        Eléctrico: débil frente a Tierra
        Hielo: débil frente a Fuego, Lucha, Roca, Acero
        Lucha: débil frente a Volador, Psíquico, Hada
        Veneno: débil frente a Tierra, Psíquico
        Tierra: débil frente a Agua, Planta, Hielo
        Volador: débil frente a Eléctrico, Hielo, Roca
        Psíquico: débil frente a Bicho, Fantasma, Siniestro
        Bicho: débil frente a Volador, Roca, Fuego
        Roca: débil frente a Agua, Planta, Lucha, Tierra, Acero
        Fantasma: débil frente a Fantasma, Siniestro
        Dragón: débil frente a Hielo, Dragón, Hada
        Siniestro: débil frente a Lucha, Bicho, Hada
        Acero: débil frente a Fuego, Lucha, Tierra
        Hada: débil frente a Veneno, Acero

        cuando se elije el ataque del usuario solo se muestra los ataques del nivel del pokemon
        si hay debilidad * 1.25
    """

    pass


def enemy_attack(my_pokemon,enemy):
    pass


def assign_exp(attacks_history):
    for pokemon in attacks_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

        while pokemon["current_exp"] > 20:
            pokemon["current_exp"] -= 20
            pokemon["level"] += 1
            pokemon["current_health"] = pokemon["base_health"]
            print("Tu pokemon ha subido al nivel {}".format(pokemon["level"]))


def choose_action():
    pass


def fight(profile, enemy_pokemon):

    print("--- NUEVO COMBATE ---")
    print("Lucharas contra {}".format(pokemon_info(enemy_pokemon)))
    print("\n"+"ELEGI TU POKEMON:")
    election_pokemon = choose_pokemon(profile)
    print("{} VS {}".format(election_pokemon["name"], enemy_pokemon["name"]))
    attack_history = []
    while any_player_pokemon_lives(profile) and enemy_pokemon["current_health"] > 0:
        print("COMIENZA --> {}".format(election_pokemon["name"]))
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = str(input("¿Que deseas hacer?: [A]tacar, [P]okeball, Pocion de [V]ida, [C]ambiar"))


        if action == "A":
            player_attack(election_pokemon, enemy_pokemon)
            attack_history.append(election_pokemon)
        elif action == "V":
            #Cura al pokemon 50 de vida si hay curas
            cure_pokemon(election_pokemon)
        elif action == "P":
            #Si el usuario tiene pokeballs intentamos capturar el pokemon
            #con una probabilidad relativa a la salud
            capture_with_pokeball(profile, enemy_pokemon)
        elif action == "C":
            #el usuario cambia de pokemon
            election_pokemon = choose_pokemon(profile)

        enemy_attack(election_pokemon, enemy_pokemon)
        if election_pokemon["current_health"] == 0 and any_player_pokemon_lives(profile):
            election_pokemon = choose_pokemon(profile)


    if enemy_pokemon["current_health"] == 0:
        print("HAS GANADO!!")
        assign_exp(attack_history)
    print("--- FIN DEL COMBATE ---")
    input("Presiona ENTER tecla para continuar")


def item_lottery():
    #Segun el factor aletorio el jugador recibe una cura o una pokeball
    pass


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    pprint(player_profile)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
        item_lottery()

    print("Has perdido en el combate numero {}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()
