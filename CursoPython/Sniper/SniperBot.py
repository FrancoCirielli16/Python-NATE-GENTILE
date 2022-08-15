from time import sleep
from requests_html import HTMLSession, AsyncHTMLSession


URL = "https://www.amazon.com/-/es/GeForce-192-bit-tarjeta-compacta-ZT-T16600K-10M/dp/B07XV7FNR2/ref=sr_1_10?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2Z87VSG83D5EA&keywords=graphics&qid=1660523908&sprefix=grafic%2Caps%2C329&sr=8-10"
session = HTMLSession()
while True:
    page = session.get(URL)
    buy_zone = page.html.find('#submit.buy-now')
    if len(buy_zone) > 0:
        print("Hay stock")
    else:
        print("No hay stock")
    sleep(1)