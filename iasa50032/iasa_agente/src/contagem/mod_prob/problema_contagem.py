from contagem.mod_prob.estado_contagem import EstadoContagem #import da classe EstadoContagem
from contagem.mod_prob.operador_incremento import OperadorIncremento #import da classe OperadorIncremento
from mod.problema import Problema #import da classe Problema

'''
Esta classe vai tratar do problema/cenário tendo um valor inicial, um valor final e uma lista de incrementos.
'''

class ProblemaContagem(Problema):

    '''
    O método construtor da superclasse é chamado e vai receber um valor inicial, 
    valor final e uma lista de incrementos como parâmetros. 
    Vamos criar uma instância da classe EstadoContagem, utilizando o valor inicial como argumento. 
    Repetimos este procedimento para cada iterador, instanciando-os através da classe OperadorIncremento.
    '''
    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(EstadoContagem(valor_inicial), [OperadorIncremento(incremento) for incremento in incrementos])
        self.__valor_final = valor_final


    #método que indica quando um estado é objetivo
    def objectivo(self, estado):
        return estado.id_valor() >= self.__valor_final