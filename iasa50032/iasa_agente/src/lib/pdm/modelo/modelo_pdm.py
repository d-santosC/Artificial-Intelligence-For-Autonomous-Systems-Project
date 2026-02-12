from abc import ABC, abstractmethod #importar metodo abstrato

'''
Interface para o processo de decisão Markov (PDM).
A propriedade de Markov estabelece que os estados futuros dependem exclusivamente do estado atual, 
não tendo qualquer influência dos estados anteriores.
'''


class ModeloPDM(ABC):

    #método que retorna os estados 
    @abstractmethod
    def S(self):
        raise NotImplementedError
    
    #método que retorna as ações do estado
    @abstractmethod
    def A(self, s):
        raise NotImplementedError
    
    #método que retorna a probabilidade quando se transita de um estado para outro
    @abstractmethod
    def T(self, s, a, sn):
        raise NotImplementedError
    
    #método que retorna a recompensa da transição
    @abstractmethod
    def R(self, s, a, sn):
        raise NotImplementedError
    
    #método que retorna os estados sucessores
    def suc(self, s, a):
        raise NotImplementedError