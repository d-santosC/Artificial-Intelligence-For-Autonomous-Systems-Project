from abc import ABC, abstractmethod #importar metodo abstrato

'''
Classe que nos permite inserir e remover nós de forma ordenada no raciocínio automático com base em PEE (Procura em Espaços de Estados),
e indica se a fronteira está vazia.
'''

class Fronteira(ABC):

    #construtor da classe onde iniciamos a fronteira
    def __init__(self):
        self.iniciar()

    #metodo onde inicializamos a lista de nós
    def iniciar(self):
        self._nos = []
    

    @abstractmethod
    def inserir(self, no):
        raise NotImplementedError
    
    #metodo que remove o primeiro elemento da lista
    def remover(self):
        if self._nos:
            return self._nos.pop(0) #utilizamos a função pop que remove um determinado elemento num index especifico
        return None
    
    #propriedade que permite retornar o número de nós (dimensão da fronteira)
    @property
    def propriedade(self):
        #se houverem nós vai retornar a dimensão
        if self._nos:
            return len(self._nos)
        return None
    
    @property
    def vazia(self):
        return len(self._nos) == 0