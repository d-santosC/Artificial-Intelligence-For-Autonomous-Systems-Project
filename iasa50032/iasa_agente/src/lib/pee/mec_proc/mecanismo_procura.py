from abc import ABC, abstractmethod #importar metodo abstrato
from pee.mec_proc.no import No #import da classe No
from pee.mec_proc.solucao import Solucao #import da classe Solucao

'''
Esta classe abstrata serve para podermos explorar o espaço de estados até encontrar o objetivo para o problema.
Um mecanismo de procura permite procurar uma solução para um problema
Utiliza uma fronteira de exploração para memorizar e gerir nós explorados

De modo a manter a informação gerada em cada passo da procura, usamos uma estrutura chamada árvore de procura. 
Esta é uma estrutura em árvore composta por nós, cada um mantendo informações sobre uma transição de estado explorada. 
Cada nó está relacionado ao seu antecessor e armazena informações sobre o estado correspondente ao nó 
e o operador que gerou a transição de estado, resultando no novo estado.
'''

class MecanismoProcura(ABC):

    #construtor da classe onde inicializamos a fronteira
    #num mecanismo de procura temos diferentes tipos de fronteiras (profundidade, largura...)
    def __init__(self, fronteira):
        self._fronteira = fronteira
    
    #metodo para iniciar a fronteira
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    
    #metodo abstrato que irá memorizar um nó
    @abstractmethod
    def _memorizar(self, no):
        raise NotImplementedError
    
    
    #metodo onde exploramos o espaço de estados começando pelo estado inicial
    #Esse espaço de estados é representado por um grafo, onde cada vértice representa um estado e cada aresta representa uma transição entre estados
    def procurar(self, problema):
        self._iniciar_memoria() #iniciamos a memoria
        no = No(problema.estado_inicial) #criamos um novo no
        self._memorizar(no) #vamos guardar o no

        #loop enquanto a fronteira não estiver vazia 
        while not self._fronteira.vazia:
             
            no = self._fronteira.remover() #removemos o primeiro no da fronteira
            
            #verificamos se estado do nó é objectivo, se for retorna a solução que termina no nó
            if problema.objectivo(no.estado):
                return Solucao(no)
            
            #para cada no sucessor inserimos o no na fronteira
            for no_suc in self._expandir(problema, no):
                #self._fronteira.inserir(no_suc)
                self._memorizar(no_suc)
        return None


    #metodo que tem como objetivo expandir um no quando se aplicam os operadores de um problema 
    #origina novos nós provenientes do nó original
    def _expandir(self, problema, no):
        suc = [] #lista de nós sucessores
        estado = no.estado #estado de um no

        #percorremos cada operador nos operadores de um problema
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado) #estado sucessor resulta da aplicação do estado ao operador

            #se um no sucessor existir calculamos o custo do no sucessor e adicionamos á lista
            if estado_suc: 

                #calculo do custo (custo até ao nó antecessor + custo da transição para o estado sucessor)
                custo = no.custo + operador.custo(estado, estado_suc)

                no_successor = No(estado_suc, operador, no, custo) #geramos um no sucessor

                suc.append(no_successor) #juntamos o no sucessor á lista de nos sucessores

        return suc