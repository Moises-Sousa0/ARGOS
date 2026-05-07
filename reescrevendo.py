import os
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as entrada:
    print("Fale!")
    audio = r.listen(entrada)

try:
    print("\nVocê falou: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("não foi possivel entender :/")
except sr.RequestError:
    print("n foi possivel se conectar")


print("a")