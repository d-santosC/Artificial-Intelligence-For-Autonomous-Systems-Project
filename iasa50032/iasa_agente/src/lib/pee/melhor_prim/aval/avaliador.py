from abc import ABC, abstractmethod #importar metodo abstrato

#Um avaliador vai avaliar o custo do percurso do nó, escolhendo o que tem menor custo

class Avaliador(ABC):

    @abstractmethod
    def prioridade(self, no):
        raise NotImplementedError