from abc import ABC, abstractmethod #importar metodo abstrato

'''
Heurísticas são abordagens eficientes para estimar valores ou resolver problemas,
dão uma estimativa do custo de um percurso desde um determinado nó até um nó objetivo

Vai refletir conhecimento acerca do domínio do problema, para guiar a procura
Boa solução para situações onde não é possível encontrar a solução ótima de forma eficiente ou prática
Heuristica também se adptam facilmente, ou seja, podem ajustar a sua abordagem dependendo nas características do problema
'''

class Heuristica(ABC):

    @abstractmethod
    def h(self, estado):
        raise NotImplementedError