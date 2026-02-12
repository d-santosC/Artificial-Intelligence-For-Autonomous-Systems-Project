from random import choice #importar função choice do módulo random em Python, que irá devolver um elemento aleatorio da lista
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover  #importar classe RespostaMover
from ecr.comportamento import Comportamento #importar classe Comportamento
from sae import Direccao #importar a classe Direccao

'''
O objetivo do comportamento "explorar" é fazer o agente se movimentar aleatoriamente,
exploranto o ambiente ao seu redor 
'''

class Explorar(Comportamento):

    
    #metodo que cria uma resposta de movimento e a ativa
    def activar(self, percepcao):
        resposta = RespostaMover(Explorar.direccao_aleatoria(self)) #criamos uma instância da classe RespostaMover
        return resposta.activar(percepcao) #ativamos a resposta apenas com um valor de percepcao porque a intensidade é um valor por omissão
    
    #metodo que cria uma direção aleatoria retirando um valor de uma lista
    def direccao_aleatoria(self):
        direccoes = list(Direccao) #lista de todas as direções possiveis
        return choice(direccoes) #retornamos uma direção aleatoria através da função choice