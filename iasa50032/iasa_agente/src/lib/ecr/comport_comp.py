from ecr.comportamento import Comportamento #importar interface Comportamento
from abc import abstractclassmethod #importar metodo abstrato

#Acções são directamente activadas em função das percepções

'''
Um comportamento pode ser composto por outros (comportamento composto) 
Como num comportamento composto temos vários comportamentos, 
é necessário um mecanismo de selecção de acção para determinar a acção a realizar
em função das respostas dos vários comportamentos internos
'''


#classe abstrata do mecanismo base de um comportamento composto que implementa a interface Comportamento
class ComportComp(Comportamento):

    #construtor da classe onde inicializamos uma lista de comportamentos
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
    
    def activar(self, percepcao):

        accoes = [] #lista de ações

        #percorremos os comportamentos, ativando-os sucessivamente e guardando cada ação numa lista de ações
        for i in self.__comportamentos:

            accao = i.activar(percepcao) #para cada comportamento vamos ativa-lo utilizando uma percepção

            #se a ação existir adicionamos á lista de ações
            #fazemos só "if accao" pq o python automaticamente converte a instancia de ação para um valor booleano
            if accao:
                accoes.append(accao) #.append para adicionar á lista de ações
        
        #se a lista de ações não for null, utilizamos o metodo que selecionar uma ação
        if accoes:
            return self.selecionar_accao(accoes)

    #metodo abstrato para selecionar uma ação 
    @abstractclassmethod
    def selecionar_accao(self, accoes):
        """..."""