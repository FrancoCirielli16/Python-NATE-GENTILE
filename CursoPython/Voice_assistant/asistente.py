import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("voice", "spanish")
engine.say("HOla")
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
