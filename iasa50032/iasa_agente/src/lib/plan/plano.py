from abc import ABC, abstractmethod #importar metodo abstrato

class Plano(ABC):

    #método que vai receber um estado e vai retornar uma ação
    @abstractmethod
    def obter_accao(self, estado):
        raise NotImplementedError

    #método que irá permitir a visualição do plano
    @abstractmethod
    def mostrar(self, vista):
        raise NotImplementedError