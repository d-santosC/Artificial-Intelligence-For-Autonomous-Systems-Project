from mod.estado import Estado #import da interface Estado

'''
EstadoAgente vai ser um tipo de estado logo vai herdar da classe Estado
Esta classe vai representar uma posição do agente
'''

class EstadoAgente(Estado):

    #construtor da classe que vai receber e guardar a posição
    def __init__(self, posicao):
        self.__posicao = posicao
    
    @property
    def posicao(self):
        return self.__posicao
    
    #método que retorna um valor hash de cada posição
    def id_valor(self):
        return hash(self.__posicao)