import os #interagir com sistema
import speech_recognition as sr #as sr serve pra criar um apelido para biblioteca



r = sr.Recognizer() #cerebro do programa, um objeto que possui metodos
transc = ""

print("Fale!")
while transc != "sair": 
    with sr.Microphone() as entrada: #abre o microfone e cria a referencia "entrada"
        

        r.adjust_for_ambient_noise(entrada) #fazer reconhecimento de ruido para se adaptar ao ambiente

        audio = r.listen(entrada) #ouve ate detectar silencio e salva o audio
        
    try:
        transc = (r.recognize_google(audio, language='pt-BR')) #aqui manda o audio pro google e recebe o texto
        print("\n" + transc) #printa o resultado do que o google mandou
    except sr.UnknownValueError: #quando não entende o que foi dito
        print("não foi possivel entender")
    except sr.RequestError as e: #quando não se comunica com google
        print("sem resultados para essa fala; {0}" .format(e))






print("\n\n --ARGOS TESTES-- ")

