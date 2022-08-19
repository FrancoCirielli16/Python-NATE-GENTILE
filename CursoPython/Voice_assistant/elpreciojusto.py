from speak_and_listen import speak, hear_me
from requests_html import HTMLSession


def main():
    speak("Bienvendio al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main_site = session.get(URL)
    categories = main_site.html.find("")

if __name__ == "__main__":
    main()
