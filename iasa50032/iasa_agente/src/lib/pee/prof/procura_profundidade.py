from pee.mec_proc.mecanismo_procura import MecanismoProcura #import da classe MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO #import da classe FronteiraLIFO

'''
Numa procura em profundidade, exploramos primeiro os nós mais recentes, aumentando por isso a profundidade do ramo corrente de procura.
Como procuramos o último elemento a ser inserido em primeiro lugar, usamos a fronteira LIFO (Last In First Out).
'''

class ProcuraProfundidade(MecanismoProcura):

    #no construtor da classe vamos ativar o construtor do MecanimosProcura e
    #passamos uma instância da fronteira em profundidade como argumento
    def __init__(self):
        super().__init__(FronteiraLIFO()) 
    
    #método onde vamos inserir o nó na fronteira
    def _memorizar(self, no):
       self._fronteira.inserir(no)
