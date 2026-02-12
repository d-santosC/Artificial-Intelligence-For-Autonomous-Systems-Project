from pee.mec_proc.fronteira import Fronteira #import da interface Fronteira

'''
Esta classe é uma forma de procura onde o último nó a ser adicionado à árvore é o primeiro a ser explorado (Last In First Out). 
Vai extender de Fronteira já que é um tipo de fronteira
'''

class FronteiraLIFO(Fronteira):

    def __init__(self):
        super().__init__()
    
    #método que vai inserir o nó na ultima posição da fronteira de exploração 
    def inserir(self, no):
        self._nos.append(no)
