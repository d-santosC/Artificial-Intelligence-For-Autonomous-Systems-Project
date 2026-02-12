from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur #import da classe AvaliadorHeur

'''
O avaliador sof vai pertencer à pesquisa sôfrega onde pretendemos minimizar a estimativa de custo para atingir o objetivo
'''

class AvaliadorSof(AvaliadorHeur):

    #método que apenas retorna a heuristica do estado do nó
    def prioridade(self, no):
        return self._heuristica.h(no.estado)