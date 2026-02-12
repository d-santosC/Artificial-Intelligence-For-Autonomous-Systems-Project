from operator import index #import da ferramente index
from pee.mec_proc.passo_solucao import PassoSolucao

'''
Classe que representa um percurso correspondente a uma solução de um problema. 
Por outras palavras, ela cria uma lista contendo todos os nós que compõem o percurso da solução.
'''

class Solucao():

    '''
    O construtor da classe vai receber o nó final e estabelece o caminho até o nó raiz, a menos que o nó final seja o próprio nó raiz.
    Criamos uma lista onde se coloca o nó final recebido na última posição.
    Criamos uma variável privada para armazenar o nó antecessor ao recebido.
    Se houver um nó antecessor, entramos num ciclo while, que insere o passo solução na primeira posição da lista de percurso
    Repetimos o processo até não haver mais nós antecessores.
    '''

    def __init__(self, no_final):
        self._no_final = no_final #Correção 1: inicializar o no_final
        no = no_final
        self.__passos = []

        #Correção 2: é o no antecessor e não o no
        while no.antecessor:
            #Correção 3: temos de criar um passo como uma instância de passo solução,
            passo = PassoSolucao(no.antecessor.estado, no.operador) 

            self.__passos.insert(0, passo) #Correção 4: vamos inserir o passo no inicio e não o nó
            no = no.antecessor

    #método que devolve o iterador de passos
    #a classe automaticamente passa a iterator
    def __iter__(self):
        return iter(self.__passos)
    
    '''
    Este método "getitem" é um método predefinido do python e vai ser utilizado para obtermos um objeto 
    de uma lista de objetos e do índice onde este objeto se encontra. 
    Utilizamos o método getitem com containers (listas, tuplos...)
    '''
    def __getitem__(self):
        return self.__passos[index]
    
    #propriedade read only que retorna a dimensão do percurso
    @property
    def dimensão(self):
        return len(self._percurso)
    
    #propriedade read only que retorna o custo de executar uma ação
    @property
    def custo(self):
        return self.custo