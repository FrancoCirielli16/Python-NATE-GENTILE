from time import sleep

import requests
import requests_html
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By

USER = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

def comprobarStockAMAZON(URL):
    r = HTMLSession()
    while True:
        page = r.get(URL, headers=USER)
        buy_zone = page.html.find('#buyNow')
        print(buy_zone)
        if len(buy_zone) > 0:
            print("Hay stock")
            try:
                driver = webdriver.Firefox()
                driver.get(URL)
                driver.find_element(By.ID, "buy-now-button").click()
                sleep(1)
                driver.find_element(By.ID, "ap_email").send_keys("ciriellifrancogiovanni@gmail.com")
                driver.find_element(By.ID, "continue").click()
                sleep(1)
                driver.find_element(By.ID, "ap_password").send_keys("Franco1605")
                driver.find_element(By.ID, "signInSubmit").click()
                print("Procesar Pago")
            except:
                print("Algo fallo")
            break
        else:
            print("No hay stock")
        sleep(3)

def comprobarStockCoolmod(URL):
    stock = ""
    while True:
        r = HTMLSession()
        page = r.get(URL, headers=USER)
        buy_zone = str(page.html.find("#messageStock"))
        print(buy_zone)
        for txt in buy_zone[43:45]:
            stock = stock + txt
        print(stock)
        if (stock == "on"):
            print("hay stock")
            try:
                driver = webdriver.Firefox()
                driver.get(URL)
                driver.find_element(By.ID, "").click()
                sleep(1)
                driver.find_element(By.ID, "").send_keys("ciriellifrancogiovanni@gmail.com")
                driver.find_element(By.ID, "").click()
                sleep(1)
                driver.find_element(By.ID, "").send_keys("Franco1605")
                driver.find_element(By.ID, "").click()
            except:
                print("Algo fallo")
            break
        else:
            print("No hay stock")
        sleep(30)


def main():
    URLa = "https://www.amazon.com/-/es/GeForce-Gaming-Tarjeta-gr%C3%A1fica-ventilador/dp/B0971XRQR4/ref=sr_1_35?keywords=graphics+card&qid=1660740253&sprefix=tarje%2Caps%2C266&sr=8-35"
    URLpc = "https://www.pccomponentes.com/hp-victus-16-e0101ns-amd-ryzen-7-5800h-16gb-512gb-ssd-rtx-3060-161"
    URLc = "https://www.coolmod.com/corsair-sabre-rgb-pro-champions-series-gaming-18000-dpi-raton/"
    comprobarStockAMAZON(URLa)
    #comprobarStockCoolmod(URLc)



if __name__ == "__main__":
    main()