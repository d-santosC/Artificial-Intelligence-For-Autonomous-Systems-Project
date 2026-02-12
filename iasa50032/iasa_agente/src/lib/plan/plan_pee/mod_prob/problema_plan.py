from mod.problema import Problema #import da interface Problema

'''
o ProblemaPlan é um tipo de problema onde realizamos um plano dependendo do custo do objetivo em si
'''

class ProblemaPlan(Problema):

    #construtor da classe onde vamos inicializar o construtor da superclasse com o estado 
    #e os operadores do modelo plano
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    #método que verifica se é objetivo, fazendo apenas a comparação entre o estado atual e o estado final
    def objectivo(self, estado):
        if estado == self.__estado_final:
            return True
        return False