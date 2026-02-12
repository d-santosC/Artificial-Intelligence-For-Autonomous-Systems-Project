from abc import ABC, abstractmethod #importar metodo abstrato

'''
Classe que faz parte do modelo de um problema, sendo o Estado o primeiro ponto do problema.
Um estado define a estrutura do problema.
A identificação de um estado é determinada pelo conjunto de informações que o define
'''

class Estado(ABC):
    
    #metodo para calcular o hash do estado, 
    #o método __hash__() recebe um objeto e retorna o valor do hash (valor representativo) como um valor int
    def __hash__(self):
        return self.id_valor()

    #metodo equals para fazer a comparação entre estados
    def __eq__(self, other):
        #se o outro objeto é um estado retorna true e se não for retorna false
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()


    #metodo abstrato para obter o id unico do valor do estado
    @abstractmethod
    def id_valor():
        raise NotImplementedError