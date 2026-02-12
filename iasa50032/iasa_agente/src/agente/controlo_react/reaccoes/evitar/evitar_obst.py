from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir #import da classe EvitarDir
from agente.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia #import da classe Hierarquia
from sae.ambiente.direccao import Direccao #import da classe Direccao

'''
O objetivo do comportamento "evitar obstaculo" é fazer o agente evitar os obstaculos que encontra á medida que
explora o ambiente nas 4 direcções possiveis
'''

class EvitarObst(Hierarquia):
    
    #construtor da classe
    def __init__(self):
         
        self._respostaEvitar = RespostaEvitar() #instancia de resposta
        #lista de comportamentos para o alvo poder evitar em diferentes direções
        comportamentos = [EvitarDir(direccao, self._respostaEvitar) for direccao in Direccao] #for para percorrer todas as direções em Direccao
        super().__init__(comportamentos) #chamamos o construtor da classe Hierarquia com os comportamentos anteriores
