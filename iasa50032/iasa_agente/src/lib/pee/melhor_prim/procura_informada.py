from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

'''
A procura informada é uma especialização da Procura Melhor Primeiro 
Utilizamos uma heurística para obter a estimativa do custo
Uma procura informada utiliza o conhecimento do dominio do problema
'''

class ProcuraInformada(ProcuraMelhorPrim):

    #neste método vamos utilizar o método "procurar" da classe ProcuraMelhorPrim
    #e do "avaliador heuristica" vamos utilizar o metodo "definir_heuristica"
    #para alterar a heuristica do próprio avaliador
    def procurar(self, problema, heuristica):
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
    