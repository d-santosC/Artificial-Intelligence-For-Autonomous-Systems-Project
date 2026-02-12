from pee.mec_proc.procura_grafo import ProcuraGrafo #import da classe ProcuraGrafo
from pee.mec_proc.solucao import Solucao #import da classe Solucao
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade #import da classe FronteiraPrioridade

'''
Classe para um mecanismo de procura do tipo de procura em grafo.
Utilizamos uma função f(n) para avaliação de cada nó gerado.
f(n) representa uma avaliação do custo da solução através do nó n
quanto menor o valor de f(n) mais promissor é o nó n
'''

class ProcuraMelhorPrim(ProcuraGrafo):

    #construtor da classe onde inicializamos uma fronteira prioridade com o parâmetro avaliador que recebemos
    def __init__(self, avaliador):
        self._avaliador = avaliador
        super().__init__(FronteiraPrioridade(self._avaliador))
    
    #método onde vamos verificar, se o custo do nó recebido é menor do que o custo do nó com o mesmo estado
    def _manter(self, no):

        return super()._manter(no) or \
            no.custo < self._explorados[no.estado].custo