from abc import ABC, abstractmethod #importar metodo abstrato

'''
Classe que representa um problema no contexto de raciocínio automático.
Um problema é o terceiro e último ponto de um modelo de raciocínio automático.
Refere-se à capacidade de um sistema computacional resolver automaticamente um problema
com base numa representação do conhecimento do respectivo domínio, produzindo uma
solução a partir de diversas alternativas possíveis.
'''


class Problema(ABC):

    #construtor da classe onde inicializamos o estaod inicial do problema e uma lista de operadores disponíveis para esse problema
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores 
    
    #metodo abstrato para saber se um estado atingiu o objetivo
    @abstractmethod
    def objectivo(self, estado):
        '''raise NotImplementedError'''
    
    #método que retorna o estado inicial
    #utilizamos o @property para transformar o método num método de leitura
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    #metodo que retorna a lista de operadores disponiveis
    @property
    def operadores(self):
        return self.__operadores