import re
from speak_and_listen import speak, hear_me

import pyttsx3
import speech_recognition as sr



def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "me llaman ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
       try:
            name = re.findall(pattern, text)[0]
       except IndexError:
            pass
    return name



def speek_with_assistan():
    speak("Hola como te llamas")
    r = sr.Recognizer()
    text = hear_me()
    name = identify_name(text.lower())
    if name:
        speak("Encantado de conocerte {}".format(name))
    else:
        speak("No te entendi un carajo podes repetirme tu nombre?")


def main():
    speek_with_assistan()


if __name__ == "__main__":
    main()