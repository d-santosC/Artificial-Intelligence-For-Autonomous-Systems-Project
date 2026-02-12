from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA #import da classe AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada #import da classe ProcuraInformada

'''
Para uma Procura A* ser ótima tem de ter um heuristica admissivel que é uma heuristica otimista
onde a estimativa é menor ou igual ao custo real

Procura A* é uma procura informada, isto é, utiliza o conhecimento do dominio do problema e
tem como objetivo minimizar o custo global
'''

class ProcuraAA(ProcuraInformada):

    #o construtor apenas vai inicializar o avaliador
    def __init__(self):
        super().__init__(AvaliadorAA())