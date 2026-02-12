from pee.prof.procura_profundidade import ProcuraProfundidade #import da classe ProcuraProfundidade

'''
Esta classe vai ser uma procura em profundidade, onde vamos limitar a procura até uma determinada quantidade de nós.
'''

class ProcuraProfLim(ProcuraProfundidade):

    #construtor da classe onde inicializamos uma variável com o valor da profundidade máxima
    def __init__(self, prof_max):
        super().__init__()
        self.__prof_max = prof_max

    #método que irá expandir o nó se a sua profundidade é mais pequena do que a profundidade máxima
    def expandir(self, problema, no):
        fronteira = []
        if (no.profundidade < self.__prof_max):
             for no.sucessor in self._expandir(problema, no):
                  fronteira._inserir(no)
                  return fronteira

    #métodos getter e setter da variável prof_max:

    @property
    def prof_max(self):
        return self.__prof_max

    @prof_max.setter
    def prof_max(self,valor):
	    self.__prof_max = valor

    