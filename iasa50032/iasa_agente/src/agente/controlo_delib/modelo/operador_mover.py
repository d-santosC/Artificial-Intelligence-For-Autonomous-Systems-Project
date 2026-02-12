import math #import do modulo math para utilizar a função dist
from agente.controlo_delib.modelo.estado_agente import EstadoAgente #import da classe EstadoAgente
from mod.operador import Operador #import da classe Operador
from sae.agente.accao import Accao #import da classe Accao

'''
A classe OperadorMover é um conceito que representa as ações que podem se relizadas no dominio do problema, 
as ações que o agente pode fazer serão mover-se nas 4 direções possiveis (norte, sul, este e oeste)
'''

class OperadorMover(Operador):

    #construtor da classe onde recebemos e guardamos o modelo mundo e direccao e
    #onde criamos uma instância de ação
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.direccao = direccao
        self.__accao = Accao(direccao) 
        
        self.__ang = self.__accao.ang


    #método onde vamor calcular a nova posição do estado e inicializamos um novo EstadoAgente com essa nova posição
    def aplicar(self, estado):
        passo = self.__accao.passo

        self.dx = round(passo * math.cos(self.ang))
        self.dy = -round(passo * math.sin(self.ang))

        self.nova_posicao = (estado.posicao[0] + self.dx, estado.posicao[1]+ self.dy)
        
        if EstadoAgente(self.nova_posicao) in self.__modelo_mundo.obter_estados():
            return EstadoAgente(self.nova_posicao)

    #método que devolve o custo necessário para passar do estado atual para o estado sucessor
    def custo(self, estado, estado_suc):
        return math.dist(estado.posicao, estado_suc.posicao)
    

    #propriedades read-only:

    @property
    def ang(self):
        return self.__ang
    
    @property
    def accao(self):
        return self.__accao
