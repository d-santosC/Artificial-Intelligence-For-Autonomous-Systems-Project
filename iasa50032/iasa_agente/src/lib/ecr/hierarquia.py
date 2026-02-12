from ecr.comport_comp import ComportComp #importe da classe ComportComp

'''
Uma hierarquia refere-se à organização de classes numa estrutura de herança, 
a herança permite que uma classe herde atributos e métodos de outra classe
Uma hierarquia fixa de subsunção é uma técnica de organização de comportamentos
Através desta organização, os comportamentos mais específicos e reativos têm prioridade sobre os comportamentos mais gerais,
isto implica que comportamentos mais específicos podem ser suprimir ou substituir as ações de comportamentos mais gerais
Uma hierarquia de subsunção é considerada "fixa" porque é definida pelo programador
'''

class Hierarquia(ComportComp):

    #metodo para selecionar uma ação
    def selecionar_accao(self, accoes):
        #verificamos se existem ações
        if accoes:
            accao = accoes[0] #selecionamos a primeira ação da lista
            return accao #retornamos a ação selecionada