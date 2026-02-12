from pee.melhor_prim.aval.avaliador import Avaliador #import da interface Avaliador

'''
Classe que representa o avaliador utilizado na pesquisa de custo uniforme
'''

class AvaliadorCustoUnif(Avaliador):
    
    #método que apenas retorna o custo do nó recebido, já que
    #a prioridade depende apenas do custo de cada nó
    def prioridade(self, no):
        return no.custo
