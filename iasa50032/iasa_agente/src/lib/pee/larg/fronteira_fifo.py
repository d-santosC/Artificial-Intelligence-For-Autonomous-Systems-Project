from pee.mec_proc.fronteira import Fronteira #import da interface Fronteira

'''
Esta classe é uma forma de procura onde o primeiro elemento a entrar vai ser o primero a sair, 
e o último a entrar será o último a sair (First In First Out).
Vai extender de Fronteira já que é um tipo de fronteira
'''

class FronteiraFIFO(Fronteira):

    def __init__(self):
        super().__init__()

    #método que vai inserir o nó na fronteira de exploração na primeira posição da lista de nós    
    def inserir(self, no):
        self._nos.insert(0, no)

