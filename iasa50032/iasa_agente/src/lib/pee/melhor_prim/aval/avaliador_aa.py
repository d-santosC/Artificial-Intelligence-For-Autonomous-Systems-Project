from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur #import da interface AvaliadorHeur

'''
O avaliador A* vai pertencer à pesquisa A* onde pretendemos minimizar o custo global
'''

class AvaliadorAA(AvaliadorHeur):

    #método que apenas retorna o custo do nó mais a heuristica do estado do nó
    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado) 