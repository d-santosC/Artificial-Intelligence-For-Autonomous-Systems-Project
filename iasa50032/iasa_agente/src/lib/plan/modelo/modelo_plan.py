from abc import ABC, abstractmethod #importar metodo abstrato

'''
A classe ModeloPlan vai permitir uma representação dos planos e ações do agente. 
Vai dar ao agente acesso à informação essencial para navegar e interagir com o ambiente de forma eficaz.
'''

class ModeloPlan(ABC):

    #método que irá retornar o estado atual
    @abstractmethod
    def obter_estado(self):
        raise NotImplementedError
    
    #método que irá retornar a lista dos estados disponiveis
    @abstractmethod
    def obter_estados(self):
        raise NotImplementedError
    
    #método que irá retornar a lista dos operadores disponiveis
    @abstractmethod
    def obter_operadores(self):
        raise NotImplementedError