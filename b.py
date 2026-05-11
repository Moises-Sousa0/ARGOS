import random

class Carta:
    def __init__(self, valor):
        self.valor = valor

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def sortear_cartas(self):
        self.mao = [Carta(random.randint(1, 10)) for _ in range(5)]

def jogar():
    # Inicializa os jogadores e suas mãos
    jogador1 = Jogador("Jogador 1")
    jogador2 = Jogador("Jogador 2")

    # Sorteia as cartas para cada jogador
    jogador1.sortear_cartas()
    jogador2.sortear_cartas()

    # Rodadas do jogo
    while True:
        # Escolhe a carta mais alta da mão de cada jogador
        carta_jogador1 = max(jogador1.mao, key=lambda x: x.valor)
        carta_jogador2 = max(jogador2.mao, key=lambda x: x.valor)

        # Imprime as cartas escolhidas
        print(f"{jogador1.nome} escolheu a carta {carta_jogador1.valor}")
        print(f"{jogador2.nome} escolheu a carta {carta_jogador2.valor}")

        # Verifica quem ganhou a rodada
        if carta_jogador1.valor > carta_jogador2.valor:
            print(f"{jogador1.nome} ganhou essa rodada!")
        elif carta_jogador1.valor < carta_jogador2.valor:
            print(f"{jogador2.nome} ganhou essa rodada!")
        else:
            print("Empate!")

        # Fim da rodada, reinicia as mãos
        jogador1.mao = []
        jogador2.mao = []

        resposta = input("Deseja jogar novamente? (s/n) ")
        if resposta.lower() != 's':
            break

if __name__ == "__main__":
    jogar()