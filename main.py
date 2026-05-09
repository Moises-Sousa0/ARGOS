import os #interagir com sistema
import speech_recognition as sr #as sr serve pra criar um apelido para biblioteca
import ollama


r = sr.Recognizer() #cerebro da transcrição, um objeto que possui metodos
transc = ""

print("Fale!")
while transc != "sair": 
    try:
        with sr.Microphone() as entrada: #abre o microfone e cria a referencia "entrada"
            r.adjust_for_ambient_noise(entrada) #fazer reconhecimento de ruido para se adaptar ao ambiente
            audio = r.listen(entrada, timeout=5) #ouve ate detectar silencio e salva o audio
            
        
        transc = (r.recognize_google(audio, language='pt-BR')) #aqui manda o audio pro google e recebe o texto            
        if transc.lower() == "sair":
            break
        mensagens = [{'role': 'user', 'content': transc}] #role seria o usario, content seria o conteudo do trans, o que foi dito
        response = ollama.chat(model='deepseek-r1:latest', messages=mensagens)
        print("\n================\n")
        print(response['message']['content']) #printa resposta do deepseek
        print("\n================\n")

    
    except sr.WaitTimeoutError: #quando usuario fica em silencio
        print("\n\nouvindo...\n")
        
    except sr.UnknownValueError: #quando não entende o que foi dito
        print("não foi possivel entender")
    except sr.RequestError as e: #quando não se comunica com google
        print("sem resultados para essa fala; {0}" .format(e))






print("\n\n --ARGOS TESTES-- ")

