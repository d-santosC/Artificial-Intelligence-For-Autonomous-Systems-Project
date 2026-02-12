from pee.melhor_prim.aval.avaliador import Avaliador #import da interface Avaliador

'''
O avaliador heur utiliza apenas utiliza uma heurística e guarda-a
'''

class AvaliadorHeur(Avaliador):

    #metodo que apena define uma heuristica
    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica