from agente.controlo_react.controlo_react import ControloReact #importar a classe ControloReact
from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.contar_passos import ContarPassos
from agente.controlo_react.reaccoes.explorar.explorar import Explorar #importar a classe Explorar
from agente.controlo_react.reaccoes.recolher import Recolher #importe da classe Recolher
from sae import Agente #importar a classe Agente

'''
Um agente reactivo é constituído por um conjunto de reações, organizadas em comportamentos, de modo a
reduzir a complexidade e a facilitar o desenvolvimento e manutenção do agente.
'''

#classe para um agente reactivo que irá derivar da classe agente
class AgenteReactivo(Agente):

    #construtor da classe
    def __init__(self):
        comportamento = Recolher() #criar uma instância da classe Explorar, o comportamento incial vai ser o de explorar
        controlo = ControloReact(comportamento) #criar uma instância da classe ControloReact, aqui definimos que o controlo do agente é baseado nas reações do comportamento
        super().__init__(controlo) #chamamos o construtor da classe Agente com o controlo anterior como argumento