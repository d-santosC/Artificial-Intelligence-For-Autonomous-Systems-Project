from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao #import da classe Prioridade


'''
O agente tem capacidade de avançar em quatro direcções (NORTE, SUL, ESTE, OESTE), logo
podemos organizar este comportamento em sub-comportamentos específicos para cada direcção
O objetivo do comportamento "aproximar alvo" é chegar mais perto do alvo mais próximo, para alcançar este objetivo, 
cada subcomportamento desse tipo, conhecido como "aproximar alvo direcional" (AproximarDir), 
precisa fornecer informações de prioridade, indicando o quão perto está o alvo detetado.
'''


class AproximarAlvo(Prioridade):

    #construtor da classe
    def __init__(self):

        #lista de comportamentos para o alvo se poder aproximar em diferentes direções
        comportamentos = [AproximarDir(direccao) for direccao in Direccao] #for para percorrer todas as direções em Direccao
        super().__init__(comportamentos) #chamamos o construtor da classe Prioridade com os comportamentos anteriores