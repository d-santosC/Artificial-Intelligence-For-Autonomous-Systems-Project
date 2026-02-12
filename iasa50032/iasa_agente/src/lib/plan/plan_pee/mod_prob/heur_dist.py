from math import dist #import da função dist do modulo math
from pee.melhor_prim.aval.heuristica import Heuristica #import da interface Heuristica

'''
A classe HeurDist é um heuristica que permite calcular uma estimativa do custo do percurso do agente 
do nó atual até ao nó do objetivo
'''

class HeurDist(Heuristica):

    #construtor que apenas recebe e guarda o estado final, que vai se o nosso objetivo
    def __init__(self, estado_final):
        self.__estado_final = estado_final

    #método onde fazemos o cálculo do custo entre o estado recebido e o estado final, utilizando a função dist
    def h(self, estado):
        return dist(estado.posicao, self.__estado_final.posicao)