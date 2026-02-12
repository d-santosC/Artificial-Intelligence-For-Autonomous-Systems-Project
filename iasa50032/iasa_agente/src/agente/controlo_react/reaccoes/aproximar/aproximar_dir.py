from agente.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo #import da classe EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover #import da classe RespostaMover
from ecr.reaccao import Reaccao #import da classe Reaccao
 

#classe que representa uma reação para aproximar numa direção específica
class AproximarDir(Reaccao):
    
    #construtor que leva como argumento a direção para a qual o agente se deve aproximar
    def __init__(self, direccao):
        estimulo = EstimuloAlvo(direccao) #instancia de estimulo
        resposta = RespostaMover(direccao) #instancia de resposta
        super().__init__(estimulo, resposta) #chamamos o construtor da classe Reaccao com o estimulo e resposta
