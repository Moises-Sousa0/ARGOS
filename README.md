🛠️ Projeto Argos
O Argos é um assistente virtual que estou desenvolvendo em Python para colocar em prática conceitos de Inteligência Artificial local, processamento de áudio e automação de sistemas.

O objetivo principal deste repositório é servir como um ambiente de estudos, onde exploro a integração de diferentes tecnologias para criar uma interface de voz funcional que rode inteiramente na minha máquina.

🧠 O que estou estudando aqui?
Este projeto é minha base para aprender e aplicar:

Backend com Python: Estruturação de projetos e lógica de automação.

IA Local: Implementação e consumo de modelos (LLMs) via Ollama.

Processamento de Linguagem Natural (NLP): Uso do Whisper para transcrição de fala em tempo real.

Sistemas e Hardware: Configuração de bibliotecas para reconhecimento de voz e uso de CUDA para aceleração por GPU.

⚡ Como o Argos funciona hoje
Atualmente, o projeto já consegue realizar o fluxo básico:

Escuta: Captura o áudio pelo microfone.

Transcrição: Transforma a fala em texto (Português) usando o Whisper.

Processamento: Envia o texto para um modelo local (Llama 3.1) que gera uma resposta.

Interface: Exibe a interação em tempo real no terminal.

Controle: Permite encerrar o processo por comandos de voz específicos.

🚀 Próximos Passos (O que pretendo implementar)
Como o projeto está em construção, estes são os desafios que quero atacar em seguida:

[ ] Memória: Fazer o Argos "lembrar" do que conversamos na mesma sessão.

[ ] Comandos de Sistema: Criar funções para ele abrir programas ou controlar o volume.

[ ] Código Modular: Refatorar o código para deixá-lo mais organizado e fácil de expandir.

[ ] Novas Integrações: Testar o uso de APIs externas e ferramentas de rede.

🛠️ Tecnologias Utilizadas
Python

OpenAI Whisper (via SpeechRecognition)

Ollama (Llama 3.1)

CUDA (NVIDIA)

📝 Nota: Este é um projeto em desenvolvimento e focado em aprendizado pessoal. Erros e refatorações constantes fazem parte do processo!
