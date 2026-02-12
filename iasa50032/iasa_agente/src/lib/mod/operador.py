from abc import ABC, abstractmethod #importar metodo abstrato

'''
Interface que faz parte do modelo de um problema, sendo o Operador o segundo ponto do problema.
Descreve uma transição entre estados: quando aplicado a um estado, 
gera um novo estado e define o custo dessa transição.
'''

class Operador(ABC):
    
    #metodo abstrato que irá receber um estado ao qual vai aplicar uma transição e retornar o estado que resulta dessa transição
    @abstractmethod
    def aplicar(self, estado):
        '''raise NotImplementedError'''
    
    #metodo abstrato que devolve o custo da transição entre dois estados
    #estado_suc -> estado sucessor
    @abstractmethod
    def custo(self, estado, estado_suc):
        ''''raise NotImplementedError'''


