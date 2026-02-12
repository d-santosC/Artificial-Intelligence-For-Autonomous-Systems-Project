from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof #import da classe AvaliadorSof
from pee.melhor_prim.procura_informada import ProcuraInformada #import da classe ProcuraInformada

'''
A Procura Sôfrega é um procura ótima onde se pretende a minimização da estimativa de custo para atingir o objetivo
Esta procura segue o caminho e se a estimativa começar a desviar a heuristicam, ela vai ter de corrigir
Não tem em conta o custo do percurso explorado
Procura Sofrêga é uma procura informada, isto é, utiliza o conhecimento do dominio do problema
'''

class ProcuraSofrega(ProcuraInformada):

    #o construtor da classe apenas vai inicializar o avaliador
    def __init__(self):
        super().__init__(AvaliadorSof())