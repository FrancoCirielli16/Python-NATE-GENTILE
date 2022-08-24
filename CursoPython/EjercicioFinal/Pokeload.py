from requests_html import HTMLSession
from bs4 import BeautifulSoup

pokemon_base = {"name": "",
                "current_health": 100,
                "base_health": 100,
                "level": 1,
                "type": [],
                "current_exp": 0

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
    print(typeF)
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

    return new_pokemon



def main():
    poke_dex = []
    for index in range(1, 100):
        poke_dex.append(get_pokemon(index))

    print(poke_dex)
if __name__ == "__main__":
    main()