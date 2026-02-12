from agente.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst #import do EstimuloObst
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover #import do RespostaMover
from ecr.reaccao import Reaccao #import da classe Reaccao

#classe que representa uma reação para evitar numa direção específica
class EvitarDir(Reaccao):

    #construtor que leva como argumento a direção para a qual o agente se deve mover para evitar
    def __init__(self, direccao, resposta):
        estimulo = EstimuloObst(direccao) #instancia de estimulo
        super().__init__(estimulo, resposta) #chamamos o construtor da classe Reaccao com o estimulo e a resposta