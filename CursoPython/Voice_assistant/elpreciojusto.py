import random
from speak_and_listen import speak, hear_me
from requests_html import HTMLSession
URL = "https://tienda.fila.com.ar/160?map=productClusterIds"
USER = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    while True:
        main_site = session.get(URL)
        categories = main_site.html.find(".glamit-fila-components-0-x-TitleLevel_3")
        print(categories)
        if categories:
            break
    category = random.choice(categories)
    for a in range(1000):
        if category.text not in ["Indumentaria", "Calzado","S","M","L","XL","XXL","XXXL","XXXXL"]:
            if category.text not in ["6", "8" ,"12" ,"14" ,"16" ,"20" ,"21" ,"22" ,"23" ,"24" ,"25" ,"26" ,"27" ,
                                     "28" ,"29" ,"30" ,"31" ,"32" ,"33" ,"34" ,"35" ,"36" ,"37" ,
                                     "38" ,"39" ,"40" ,"41" ,"42" ,"43" ,"44" ,"45"]:
                print(category.text)
        category = random.choice(categories)


if __name__ == "__main__":
    main()
