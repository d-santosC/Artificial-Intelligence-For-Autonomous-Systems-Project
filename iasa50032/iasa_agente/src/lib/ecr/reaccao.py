from ecr.comportamento import Comportamento  #importar interface Comportamento

'''  
Uma arquitectura de agentes reactivos define um ciclo percepção-reacção-acção, onde as reacções definem de forma
modular as associações entre estímulos (derivados da percepção) e respostas (geradoras de acção)

A reação é um módulo que associa estímulos a respostas
'''

#classe que irá servir para ativar uma reação do agente e implementa a interface Comportamento
class Reaccao(Comportamento):

    #construtor da classe, onde se incializa o estimulo e a resposta   
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    #metodo para ativar uma reação do agente
    def activar(self, percepcao):

        #retorna uma intensidade detetando através de um estimulo com uma percepção
        intensidade = self.__estimulo.detectar(percepcao)

        #se a intensidade anterior for maior que 0 vamos retonar uma resposta que será a nossa ação
        if intensidade > 0:
            return self.__resposta.activar(percepcao, intensidade)
        