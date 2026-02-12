from mod.estado import Estado #import da classe Estado

'''
Classe que mostra o estado das peças no tabuleiro
'''

class EstadoDoPuzzle(Estado):

    #construtor que recebe a posição das pecas (configuração)
    def __init__(self, pecas):
        self._pecas = pecas

    
    #método que retorna um valor único (hash) para as peças.
    #configuração de estado é a informação que caracteriza o estado
    def id_valor(self):
        raise NotImplementedError