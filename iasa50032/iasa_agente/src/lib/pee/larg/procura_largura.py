from pee.mec_proc.procura_grafo import ProcuraGrafo #import da classe ProcuraGrafo
from pee.prof.fronteira_lifo import FronteiraLIFO #import da classe FronteiLIFO

"""
Procuramos primeiro nos nós mais antigos
Exploramos cada nível de procura antes da exploração a um nível mais profundo
Como a procura é em fila, utilizamos a fronteira FIFO
"""

class ProcuraLargura(ProcuraGrafo):

    def __init__(self):
        _fronteira = FronteiraLIFO()
        super._init_(_fronteira)