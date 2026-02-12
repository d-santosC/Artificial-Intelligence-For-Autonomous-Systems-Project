from abc import ABC, abstractmethod #importar metodo abstrato

#Um estimulo define informação activadora de uma reacção

#interface que define a funcionalidade geral de um estímulo que herda da classe ABC
class Estimulo(ABC):

    #metodo abstrato
    @abstractmethod
    def detectar(self, percepcao):
        # raise NotImplementedError, lançar exceção de que o metodo não está concluido
        """..."""

    