import speech_recognition as sr
import whisper
from tempfile import NamedTemporaryFile
from pathlib import Path
import ollama


print("\nIniciando Argos...\n")

modelo = whisper.load_model("medium").to("cuda")
r = sr.Recognizer()
transc = ""

print("Fale!\n")

while True:
    try:

        with sr.Microphone() as entrada:
            r.adjust_for_ambient_noise(entrada)
            audio = r.listen(entrada, timeout=5)


        with NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(audio.get_wav_data())
            temppath = Path(f.name)


        resultado = modelo.transcribe(str(temppath), language='pt')
        temppath.unlink()
        transc = resultado['text']
        if len(transc.strip()) < 3:
            continue


        print(f"\nUser: {transc}")
        texto = transc.strip().lower()
        tem_argos = any(palavra in texto for palavra in ["argos", "argus", "arcus",])
        tem_sair = any(palavra in texto for palavra in ["sair", "sai", "sai!", "saí", "encerrrar", "fechar", "parar"])   
        if tem_argos and tem_sair:
            break



        print ("Pensando...")
        mensagens = [{'role': 'user', 'content': transc}]
        response = ollama.chat(model='llama3.1:latest', messages=mensagens)
        print("\n================\n")
        print(response['message']['content'])
        print("\n================\n")



    except Exception as e:
        print(type(e))