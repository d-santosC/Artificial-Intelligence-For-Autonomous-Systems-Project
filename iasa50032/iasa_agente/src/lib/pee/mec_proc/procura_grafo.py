from abc import abstractmethod #importar metodo abstrato
from pee.mec_proc.mecanismo_procura import MecanismoProcura #import da classe MecanismoProcura

'''
Esta classe vai ser a base da procura em largura e de outros metodos de procura 
em que a forma de manter a memoria é diferente.

Na procura vamos ter estados repetidos, logo para podermos eliminar de nós de estados repetidos, 
temos de verificar se um nó sucessor tem um estado que já foi explorado
'''

class ProcuraGrafo(MecanismoProcura):

    #método onde vamos iniciar a fronteira
    def _iniciar_memoria(self):
        super()._iniciar_memoria() #vamos dar override do iniciar memoria
        self._explorados = {} #dicionário de estados já explorados
    
    #método abstrato onde vamos verificar se o nó ainda não foi explorado, utilizando a função "manter" 
    #inserimos o nó à fronteira
    def _memorizar(self, no):
        if self._manter(no):
            self._fronteira.inserir(no)
            self._explorados[no.estado] = no
    
    #método onde vamos verificar se um certo nó recebido não pertence à lista de nós já explorados.
    def _manter(self, no):
        return no.estado not in self._explorados
