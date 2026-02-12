from contagem.mod_prob.estado_contagem import EstadoContagem #import da classe EstadoContagem
from mod.operador import Operador #import da classe Operador

'''
Esta classe vai ser um operador no contexto do problema
A implementação permite a execução do nosso problema, representando a transição entre estados
'''

class OperadorIncremento(Operador):

    #construtor onde recebemos e inicializamos os incrementos
    def __init__(self, incremento):
        self.__incremento = incremento
    
    #método que transforma um estado num novo estado que vai ser o valor do estado anterior mais 1
    def aplicar(self, estado):
        return EstadoContagem(estado.id_valor() + self.__incremento)
    
    #método para o custo de um operador que é o quadrado do incremento
    def custo(self, estado, estado_suc):
        return self.__incremento ** 2