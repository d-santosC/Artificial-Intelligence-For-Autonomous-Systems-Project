'''
Resposta é um tipo que define as várias acções que podem ser realizadas
Define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade
 '''

#classe que gera uma resposta 
class Resposta:

    #construtor da classe, onde incializamos uma ação
    def __init__(self, accao):
        self._accao = accao

    #metodo onde definimos a prioridade da ação associada á resposta e retornamos.
    #a intensidade tem valor por omissão de 0, este valor será usado sempre que se omite esse parametro 
    #na invocação da função
    def activar(self, percepcao, intensidade=0):

        self._accao.prioridade = intensidade #definimos a prioridade da ação igual á itensidade
        return self._accao
