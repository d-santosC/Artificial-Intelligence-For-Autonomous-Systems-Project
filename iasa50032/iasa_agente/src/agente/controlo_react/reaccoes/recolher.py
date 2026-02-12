from agente.controlo_react.reaccoes.contar_passos import ContarPassos #importe da classe ContarPassos
from .aproximar.aproximar_alvo import AproximarAlvo #importe da classe AproximarAlvo
from .evitar.evitar_obst import EvitarObst #importe da classe EvitarObst
from .explorar.explorar import Explorar #importe da classe Explorar
from ecr.hierarquia import Hierarquia #importe da classe Hierarquia

'''
classe que representa um comportamento composto que agrega um conjunto de sub-comportamentos 
O objetivo é recolher alvos, isto é realizado através de 3 comportamentos:
-aproximar alvo
-evitar objetos
-explorar ambiente

Estes comportamentos estão relacionados e organizados considerando os seguintes aspectos principais:
- 3 níveis de competência (aproximar, evitar e explorar)
- hierarquia fixa de prioridade entre comportamentos

'''

class Recolher(Hierarquia):

    #construtor da classe
    def __init__(self):
        comportamentos = [AproximarAlvo(), EvitarObst(), Explorar()] #lista dos comportamentos, por ordem de maior prioridade
        super().__init__(comportamentos) #chamamos o construtor da classe Hierarquia com os comportamentos anteriores