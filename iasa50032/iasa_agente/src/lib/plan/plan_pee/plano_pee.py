from plan.plano import Plano #import da interface Plano

'''
O PlanoPEE vai ser um tipo de plano que utiliza a Procura em Espaço de Estados (PEE).
Com base na informação do estado atual e do objetivo final, elabora-se um plano especifico para o agente, onde
temos as ações que o agente deve realizar para alcançar o objetivo de forma mais eficiente.
'''

class PlanoPEE(Plano):

    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]

    
    def obter_accao(self, estado):
        if self.__passos:
            passo = self.__passos.pop(0) 

            if passo.estado == estado:
                return passo.operador

    #método para mostrar os passos do agente
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)