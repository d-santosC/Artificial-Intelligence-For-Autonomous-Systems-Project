from abc import ABC, abstractclassmethod #importar metodo abstrato

#Um comportamento é um conjunto de reacções relacionadas entre si e
#relaciona padrões de percepção com padrões de ação

#interface que define a funcionalidade geral de um comportamento e que herda da classe ABC
class Comportamento(ABC):

    #metodo abstrato onde ativamos o comportamento dependendo da percepção
    @abstractclassmethod
    def activar(self, percepcao):
        """..."""
