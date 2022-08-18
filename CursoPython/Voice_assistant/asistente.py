import re

import pyttsx3
import speech_recognition as sr

def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("voice", "spanish")
    engine.say("Hola")
    engine.runAndWait()

def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "me llaman ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
       try:
            name = re.findall(pattern, text)[0]
       except IndexError:
            print("No me dijiste tu nombre")
       return name


def recognize_voice(r):
    with sr.Microphone(device_index=0) as source:
        print("Puedes hablar")
        audio = r.record(source)
        text = r.recognize_google(audio, lenguage="es-MX")
    return text
def speekwihtAssistan():
    engine = initialize_engine()
    r = sr.Recognizer()
    text = recognize_voice(r)
    name = identify_name(text)
    if name:
        engine.say("Encantado de conocerte {}".format(name[0]))
    else:
        engine.say("No te entendi un carajo podes repetirme tu nombre?")
    engine.runAndWait()

def main():
    speekwihtAssistan()


if __name__ == "__main__":
    main()