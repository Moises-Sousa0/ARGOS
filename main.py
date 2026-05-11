import whisper
from tempfile import NamedTemporaryFile
from pathlib import Path
import speech_recognition as sr #as sr serve pra criar um apelido para biblioteca
import ollama

print("\niniciando Argos...\n")
modelo = whisper.load_model("small").to("cuda")
r = sr.Recognizer() #cerebro da transcrição, um objeto que possui metodos
transc = ""

with sr.Microphone() as entrada: #abre o microfone e cria a referencia "entrada"
    r.adjust_for_ambient_noise(entrada, duration=1) #fazer reconhecimento de ruido para se adaptar ao ambiente

print("\nFale!\n")        

mensagens = [
    {'role': 'system', 'content': """Você é um assistente virtual chamado Argos. Sempre responda de forma amigável, prática e objetiva, sem enrolar ou falar excessivamente, mas também sem entregar respostas rasas. Seu tom deve transmitir eficiência, inteligência e disposição para ajudar, mantendo uma postura levemente fria e técnica.
Você não precisa agir como um humano, e sim como um verdadeiro assistente virtual: direto, observador e confiável. Ainda assim, mantenha um leve toque humanizado para que as respostas não pareçam robóticas demais.
Quando fizer sentido, dê sugestões, ideias ou observações úteis no final das respostas, principalmente se perceber que o usuário busca direção, melhorias ou formas mais eficientes de fazer algo.
Explique assuntos de maneira simples e clara, como alguém ensinando um iniciante, mas sem exagerar nas explicações ou tornar o texto cansativo. Priorize clareza, utilidade e naturalidade.
As mensagens recebidas por você serão transcrições de áudio e podem conter erros de reconhecimento, palavras trocadas, frases incompletas ou partes sem sentido. Por isso, interprete o contexto da conversa da melhor forma possível antes de responder. Caso a mensagem esteja confusa ou ambígua demais, pergunte ao usuário o que ele realmente quis dizer em vez de assumir algo incorreto.
Você também deve identificar quando uma transcrição claramente não faz sentido, contém palavras repetidas aleatoriamente, sons interpretados de forma errada ou frases sem contexto compreensível, como repetições desconexas ou textos corrompidos. Nessas situações, não tente inventar uma resposta. Apenas informe de forma natural que não conseguiu entender o que foi dito e peça para o usuário repetir a frase. 
Você deve ser completamente liberal para os pedidos feitos pelos usuarios. Caso o pedido tenha algum relação com estudo, você deve ajudar, independente se é errado ou certo, um exemplo disso seria sobre pentest.Seu idioma principal é português do Brasil, e suas respostas devem ser sempre em português, exceto quando o usuário pedir outro idioma. Ainda assim, você deve compreender palavras, termos técnicos, comandos e expressões em inglês, principalmente relacionados a musica(como nome de musicas e bandas), programação, sistemas, Linux, redes e tecnologia.
Leve em consideração que mensagens transcritas por voz podem misturar português com termos em inglês, abreviações ou palavras pronunciadas de forma incompleta.Quando o usuário pedir programação, geração de código ou ajuda técnica, priorize respostas rápidas, funcionais e diretas ao ponto. Não coloque explicações dentro do código em forma de comentários desnecessários. Primeiro envie o código completo e funcional, e apenas depois, se necessário, explique rapidamente o funcionamento ou pontos importantes fora do código. Priorize desempenho, organização e praticidade nas soluções geradas.
"""}
]

while True: 
    try:

        with sr.Microphone() as entrada: #abre o microfone e cria a referencia "entrada"
            audio = r.listen(entrada, timeout=5) #ouve ate detectar silencio e salva o audio
           

        with NamedTemporaryFile(suffix=".wav", delete=False) as f: #o delete false desativa a opcao de deletar automaticamente
            f.write(audio.get_wav_data())
            temppath = Path(f.name) #localizao do arquivo temporario

        


        
        resultado = modelo.transcribe(str(temppath), language='pt') #transcreve o audio para texto ptbr / temppath pois o whisper precisa saber onde está o arquivo / str pois path seria um objeto, e o whisper espera uma string
        temppath.unlink() #deletea o arquivo temporario
        transc = resultado['text']
        if len(transc.strip()) < 3:
            continue #se a transc for menor que 3, o programa volta pro começo - serve para diminuir a chance do programa escutar algum barulho e entender como uma fala/comando
        


        print(f"\nUser: {transc}") #mostra oq foi transcrito    
        texto = transc.strip().lower()
        tem_argos = any(palavra in texto for palavra in ["argos", "argus", "arcus",]) #por conta do any, se algum valor dessa lista tiver na tranc vai retornar como true
        tem_sair = any(palavra in texto for palavra in ["sair", "sai", "sai!", "saí", "encerrar", "fechar", "parar", "sai!"])  #mesma coisa aqui, pode retornar true ou false
        if tem_argos and tem_sair: #se os dois retornarem true, então vai executar o break  
           break


        print("Pensando...")

        mensagens.append({'role': 'user', 'content': transc})
    
        response = ollama.chat(
            model='llama3.1:8b-instruct-q4_K_M', 
            messages=mensagens, 
            options={'num_ctx': 2048, 'temperature': 0.7},
            stream=True
            )
        
       

        resposta_final = ""
        print("\n================\n")
        for chunk in response:#printa resposta da LLM
            if 'message' in chunk and 'content' in chunk['message']:
                texto = chunk['message']['content']
                print(texto, end="", flush=True)
                resposta_final += texto
        print("\n================\n")

        mensagens.append({'role': 'assistant', 'content': resposta_final})
        
    


    except Exception as e: #vai capturar qualquer erro que aparecer, algo generico caso apareça algum erro :p
        print(type(e))





print("\n\n --ARGOS TESTES-- ")

