from abc import ABC, abstractmethod #importar metodo abstrato

class Planeador(ABC):
    
    '''
    metodo abstrato produz um plano que permite obter a ação a realizar de um determinado estado 
    vai precisar do modelo de planeamento que disponibiliza a informação do estado atual do sistema, 
    os estados e os operadores disponiveis
    '''
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        raise NotImplementedError