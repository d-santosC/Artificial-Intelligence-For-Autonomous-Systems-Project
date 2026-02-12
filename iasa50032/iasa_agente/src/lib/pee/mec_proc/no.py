'''
Esta classe representa um Nó que é um componente essencial da arvore de procura, armazena informações sobre 
o estado que representa, o operador que gerou esse estado, o nó antecessor na árvore de procura, 
a profundidade do nó na árvore e o custo total do percurso até o nó.
'''

class No:

    '''
    Se for um nó raiz, não terá antecessores ou operador, então por padrão serão None e os outros parâmetros,
    exceto o estado, serão todos 0.
    '''
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo

    #método que vai tornar a classe numa classe comparável
    def __lt__(self,no):
        return self.custo < no.custo


    #atributos read-only da classe:

    #se não for um nó raiz (temos antecessores), a profundidade vai ser um incremento da profundidade do antecessor por uma unidade,
    #se for, retorna 0
    @property
    def profundidade(self):
        if self.__antecessor():
            self._profundidade = self.__antecessor.profundidade() + 1
            return self._profundidade
        return 0
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor
    
    @property
    def estado(self):
        return self.__estado