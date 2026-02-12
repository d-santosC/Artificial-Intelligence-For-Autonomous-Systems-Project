from mod.estado import Estado #import da classe Estado

'''
Classe que é um tipo de Estado no contexto do problema, ou seja, o estado dos valores
'''

class EstadoContagem(Estado):

    #construtor da classe que recebe o valor
    def __init__(self, valor):
        self._valor = valor

    #método que retorna o id em int do valor
    def id_valor(self):
        return self._valor
    