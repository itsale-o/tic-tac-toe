import time
from player import JogadorHumano, AutoJogadorAleatorio

class TicTacToe:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)] # uma lista única que representa o tabuleiro 3x3
        self.vencedor_atual = None # nenhum vencedor inicialmente

    def imprimir_tabuleiro(self):
        for linha in [self.tabuleiro[(i*3):(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(linha) + ' | ')

    @staticmethod
    def imprimir_numeros_tabuleiro():
        # 0 | 1 | 2 (nos diz qual número corresponde a cada espaço)
        numero_tabuleiro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for linha in numero_tabuleiro:
            print(' | ' + ' | '.join(linha) + ' | ')

    def mov_disponiveis(self):
        # usando list comprehension
        return [i for i, lugar in enumerate(self.tabuleiro) if lugar == ' ']
        # a linha acima resume a lógica abaixo
        #  movimentos = []
        #  for (i, posicao) in enumerate(self.board):
                #['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #      if posicao == ' ':
        #         movimentos.append(i)
        #  return movimentos

    def espacos_vazios(self):
        return ' ' in self.tabuleiro

    def qtde_espacos_vazios(self):
        return self.tabuleiro.count(' ')

    def jogada(self, espaco, letra):
        # se a jogada for válida retornamos True 
        # se a jogada for inválida retornamos False
        if self.tabuleiro[espaco] == ' ':
            self.tabuleiro[espaco] = letra
            if self.vencedor(espaco, letra):
                self.vencedor_atual = letra
            return True
        return False

    def vencedor(self, espaco, letra):
        # vamos checar as linhas 
        linha_ind = espaco // 3
        linha = self.tabuleiro[linha_ind*3 : (linha_ind + 1) * 3]
        if all(lugar == letra for lugar in linha):
            return True
        
        # checando as colunas
        coluna_ind = espaco % 3
        coluna = [self.tabuleiro[coluna_ind+i*3] for i in range(3)]
        if all(lugar == letra for lugar in coluna):
            return True
        
        # checando as diagonais
        # as diagonais terão índices pares no tabuleiro (0, 2, 4, 6, 8)
        if espaco % 2 == 0:
            diagonal_1 = [self.tabuleiro[i] for i in [0, 4, 8]]
            if all(lugar == letra for lugar in diagonal_1):
                return True
            diagonal_2 = [self.tabuleiro[i] for i in [2, 4, 6]]
            if all(lugar == letra for lugar in diagonal_2):
                return True
        
        # se todos os casos falhares
        return False

def jogar(jogo, jogador_x, jogador_o, imprimir_jogo=True):
    # retorna o vencedor ou None, em caso de empate
    if imprimir_jogo:
        jogo.imprimir_numeros_tabuleiro()

    letra = 'x' # começando o jogo com x
    # iterando o código enquanto tiver espaços vazios no jogo
    # não precisamos nos preocupar com o vencedor
    while jogo.espacos_vazios():
        # queremos o movimento do jogador apropriado
        if letra == 'o':
            espaco = jogador_o.faca_a_jogada(jogo)
        else:
            espaco = jogador_x.faca_a_jogada(jogo)

            # função para fazer a jogada
        if jogo.jogada(espaco, letra):
            if imprimir_jogo:
                print(letra + f' fez uma jogada no espaço {espaco}')
                jogo.imprimir_tabuleiro()
                print('') # só uma linha vazia
                
            if jogo.vencedor_atual:
                if imprimir_jogo:
                    print(f'Tic-Tac-Toe! {letra} venceu!')
                return letra

            letra = 'o' if letra == 'x' else 'x' # mudando de jogadores
                # outra forma de escrever a linha acima:
                # if letter == 'o':
                    # letter = 'x'
                # else:
                    # letter = 'o'
        # pequena pausa entre as iterações
        time.sleep(1)
            
    if imprimir_jogo:
        print('É um empate')

if __name__ == '__main__':
    jogador_x = JogadorHumano('x')
    jogador_o = AutoJogadorAleatorio('o')
    t = TicTacToe()
    jogar(t, jogador_x, jogador_o, imprimir_jogo=True)