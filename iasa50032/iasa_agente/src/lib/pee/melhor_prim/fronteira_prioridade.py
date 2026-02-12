from heapq import heappop, heappush #import das funções heappop e heappush
from pee.mec_proc.fronteira import Fronteira #import da interface Fronteira

'''
Classe que vai ser utilizada por a Procura Melhor Primeiro
É um tipo de fronteira onde o nós inseridos têm prioridade
'''

class FronteiraPrioridade(Fronteira):

    def __init__(self, avaliador):
        self._avaliador = avaliador #alteramos a arquitetura do atributo de private para protected
    
    #método onde vamos obter a prioridade do nó recebido e, com essa prioridade, inserimos o nó na posição da lista 
    def inserir(self, no):
        prioridade = self._avaliador.prioridade(no) #obter a prioridade do nó

        #a função heappush vai inserir um novo elemento (prioridade, no),
        #que será o nó com maior prioridade, na lista self._nos
        heappush(self._nos, (prioridade, no)) 
    
    #método onde removemos o nó pela sua prioridade
    def remover(self):
        #convenção do Python, quer dizer que o valor não vai ser utilizado (_)
        _,no = heappop(self._nos) #remover o nó com menor prioridade da lista self._nos
        return no