import math
import random

class Jogador:
    def __init__(self, letra):
        # letra x ou o
        self.letra = letra

    # queremos que o jogador faça seu próximo movimento
    def faca_a_jogada(self, jogo):
        pass

class AutoJogadorAleatorio(Jogador):
    def __init__(self, letra):
        super().__init__(letra)
    
    def faca_a_jogada(self, jogo):
        espaco = random.choice(jogo.mov_disponiveis())
        return espaco

class JogadorHumano(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def faca_a_jogada(self, jogo):
        espaco_valido = False
        valor = None
        while not espaco_valido:
            espaco = input(self.letra + ' --> vez deste jogador. Indique o movimento (0 - 8): ')
            # vamos checar se o valor inserido é correto
            # se o espaco não estiver disponível vamos dizer que o valor é inválido
            try:
                valor = int(espaco)
                if valor not in jogo.mov_disponiveis():
                    raise ValueError
                espaco_valido = True
            except ValueError:
                print('Espaço indiponível. Tente novamente.')
        
        return valor