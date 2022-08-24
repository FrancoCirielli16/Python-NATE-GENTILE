import pickle
from requests_html import HTMLSession
from bs4 import BeautifulSoup

pokemon_base = {"name": "",
                "current_health": 100,
                "base_health": 100,
                "level": 1,
                "type": None,
                "current_exp": 0,
                "attacks": None

                }

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk="





def obtener_type(types):
    typeF = ""
    for img in types[5:7]:
        typeF += ","
        for data_img in img[10:19]:
            if data_img != '"' and data_img != " ":
                typeF += data_img

    return typeF



def get_pokemon(index):

    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()
    pokemon_page = session.get(url)
    soup = BeautifulSoup(pokemon_page.text, "lxml")
    new_pokemon = pokemon_base.copy()
    name = pokemon_page.html.find(".mini", first=True).text


    for char in name:
        if char != "\n":
            new_pokemon["name"] += char
        else:
            break


    types = str(soup.body.find_all("img"))
    types = types.split(",")
    typeF = obtener_type(types)
    typeF = typeF.split(",")
    new_pokemon["type"] = []
    for T in typeF:
        if T in ['planta', "veneno", "psiquico", "volador", "normal", "tierra"]:
            new_pokemon["type"].append(T)
        else:
            if T in ["fuegos", "luchas", "bichos", "hielos"]:
                new_pokemon["type"].append(T[0:5])
            else:
                if T in ["aguasr", "hadasr", "roca"]:
                    new_pokemon["type"].append(T[0:4])
                else:
                    if T in ["electric"]:
                        new_pokemon["type"].append("electrico")

    url = "{}{}".format("https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk=", index)
    session = HTMLSession()
    pokemon_page = session.get(url)
    new_pokemon["attacks"] = []
    for attacks_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attacks_item.find("td", first=True).find("a", first=True).text,
            "type": attacks_item.find("td")[1].find("img", first=True).attrs["alt"],
            "damage": int(attacks_item.find("td")[3].text.replace("--", "0")),
            "min_level": attacks_item.find("th", first=True).text,
        }
        new_pokemon["attacks"].append(attack)


    return new_pokemon



def get_all_pokemons():
    try:
        print("Cargando el archivos de pokemons...")
        with open("pokedex.pkl", "rb") as pokedex:
            all_pokemons = pickle.load(pokedex)
    except FileNotFoundError:
        print("Archivo no encontrado, cargando de internet...")
        all_pokemons = []
        for index in range(151):
            all_pokemons.append(get_pokemon(index + 1))
            print("*", end="")
        with open("pokedex.pkl", "wb") as pokedex:
            pickle.dump(all_pokemons, pokedex, -1)
        print("\n¡Todos los pokemons se descargaron...")

    print("La lista de pokemons se cargo correctamente...")
    return all_pokemons


