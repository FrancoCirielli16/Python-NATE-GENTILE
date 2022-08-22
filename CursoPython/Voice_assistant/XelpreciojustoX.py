import random

import requests

from speak_and_listen import speak, hear_me
from bs4 import BeautifulSoup
from requests_html import HTMLSession
URL = "https://tienda.fila.com.ar/"
USER = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

def obtener_categoria():
    session = HTMLSession()
    while True:
        main_site = session.get(URL, headers=USER)
        categories = main_site.html.find(".glamit-fila-components-0-x-TitleLevel_3")
        print(categories)
        if categories:
            break
    category = random.choice(categories)
    while True:
        if category.text not in ["Calzado", "Ver todos", "Ver todo", "S", "M", "L", "XL", "XXL", "XXXL", "XXXXL"]:
            if category.text not in ["6", "8", "12", "14", "16", "20", "21", "22", "23", "24", "25", "26", "27",
                                 "28", "29", "30", "31", "32", "33", "34", "35", "36", "37",
                                 "38", "39", "40", "41", "42", "43", "44", "45"]:
                print(category.text)
                break
        category = random.choice(categories)
    return category

def obtener_titulo(soup):
    title_product = soup.find_all("span", class_="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body")
    title_product = str(title_product)
    title_product = title_product.split(",")
    max = len(title_product)
    index = random.randint(0, max)
    prices = title_product[index]
    prices = [title_product[95:], index]
    return prices


def obtener_precio(soup, index):
    prices = soup.find_all("span", class_='glamit-product-price-0-x-sellingPrice glamit-product-price-0-x-sellingPriceValue t-heading-2-s dib ph2 glamit-product-price-0-x-price_sellingPrice')
    prices = str(prices)
    prices = prices.split(",")
    prices = prices[index]
    return prices[161:]

def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    category = obtener_categoria()
    print(category.text)
    while True:
        product_page = requests.get("https://tienda.fila.com.ar{}".format(category.attrs["href"]))
        print(product_page)
        soup = BeautifulSoup(product_page.text, "lxml")
        print(soup.prettify())
        if soup:
            titulo = obtener_titulo(soup)
            print(titulo[0])
            print(obtener_precio(soup, titulo[1]))
            break


if __name__ == "__main__":
    main()
