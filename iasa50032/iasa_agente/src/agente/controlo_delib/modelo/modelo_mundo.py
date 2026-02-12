import math #import do modulo math
from agente.controlo_delib.modelo.estado_agente import EstadoAgente #import da classe EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover #import da classe OperadorMover
from plan.modelo.modelo_plan import ModeloPlan #import da classe ModeloPlan
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento #import do enum Direccao

'''
Esta classe vai representar o modelo mundo, o ModeloMundo é o suporte de representação do mundo ou ambiente onde
o agente se encontra.
Permite obter o estado atual do agente, os estados do mundo, calcular a distancia e atualizar o modelo com base numa percepção

A classe MecDelib vai utilizar o modelo mundo
'''

class ModeloMundo(ModeloPlan):

    '''
    construtor da classe onde vamos inicializar uma lista de operadores gerada por significado, 
    cada elemento da lista é uma instância da classe OperadorMover, ou seja, para cada direção no enum Direccao,
    criamos um objeto OperadorMover e adicionamos à lista de operadores
    '''
    def __init__(self):
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self.__posicao = None
        self.__elementos = None
        self.__estado = None
        self.__estados = []
    
    #método que retorna o estado atual
    def obter_estado(self):
        return self.__estado
    
    #método que retorna a lista de estados
    def obter_estados(self):
        return self.__estados
    
    #método que retorna a lista de operadores
    def obter_operadores(self):
        return self.__operadores
    
    #método que vai buscar um elemento da lista de elementos
    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao)
    
    #método onde vamos calcular a distância entre o estado atual e o estado recebido
    #utilizando a função dist do módulo math
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)

    #método onde vamos fazer a atualização do mundo
    #primeiramente atualizamos o estado atual, depois atualizamos a lista de estados e os elementos
    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
        self.__elementos = percepcao.elementos #dicionario cuja chave é a posicao (x,y) 
        self.__recolha = percepcao.recolha


    #método que vai permitir a visualização da informação interna do agente
    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items(): #mostra uma lista de tuplos que representam a chave e os elementos
            #se o elemento for um alvo ou obstaculo vai mostrar no ecra
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)

        vista.marcar_posicao(self.__estado.posicao)
    
    #propriedade alterado read-only que retorna a recolha
    @property
    def alterado(self):
        return self.__recolha