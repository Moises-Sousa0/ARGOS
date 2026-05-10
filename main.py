import whisper
from tempfile import NamedTemporaryFile
from pathlib import Path
import os #interagir com sistema
import speech_recognition as sr #as sr serve pra criar um apelido para biblioteca
import ollama

modelo = whisper.load_model("medium").to("cuda")
r = sr.Recognizer() #cerebro da transcrição, um objeto que possui metodos
transc = ""

print("\nFale!\n")


while True: 
    try:

        with sr.Microphone() as entrada: #abre o microfone e cria a referencia "entrada"
            r.adjust_for_ambient_noise(entrada) #fazer reconhecimento de ruido para se adaptar ao ambiente
            audio = r.listen(entrada, timeout=5, phrase_time_limit=10) #ouve ate detectar silencio e salva o audio
           

        with NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(audio.get_wav_data())
            temppath = Path(f.name)

        


        
        resultado = modelo.transcribe(str(temppath), language='pt') #transcreve o audio para texto ptbr
        temppath.unlink() #deletea o arquivo temporario
        transc = resultado['text']
        if len(transc.strip()) < 3:
            continue
        


        print(f"\nUser: {transc}")    
        texto = transc.strip().lower()
        tem_argos = any(palavra in texto for palavra in ["argos", "argus", "arcus",]) #por conta do any, se algum valor dessa lista tiver na tranc vai retornar como true
        tem_sair = any(palavra in texto for palavra in ["sair", "sai", "sai!", "saí", "encerrar", "fechar", "parar", "sai!"])  #mesma coisa aqui, pode retornar true ou false
        if tem_argos and tem_sair: #se os dois retornarem true, então vai executar o break  
           break


        print("pensando...")
        mensagens = [{'role': 'user', 'content': transc}] #role seria o usario, content seria o conteudo do trans, o que foi dito
        response = ollama.chat(model='llama3.1:latest', messages=mensagens)
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

