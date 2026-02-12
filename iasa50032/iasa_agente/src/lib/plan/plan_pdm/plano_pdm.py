from plan.plano import Plano #import da interface Plano

'''
A classe PlanoPDM vai representar um tipo de plano baseado nos Processos de Decisão de Markov (PDM).
Com esta classe criamos um plano para o movimento do agente que leve em consideração a utilidade e a política.
'''

class PlanoPDM(Plano):

    #construtor da classe que vai receber a utilidade e a politica e inicializar as suas variaveis
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    #método onde obtemos uma ação através de um estado, sendo este obtido a partir da politica
    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
        return None
    
    '''
    método que permite visualizar os possíveis movimentos do agente no plano. 
    Se houver política, mostramos a utilidade com base no estado e valor. 
    Também mostramos a política como um vetor, utilizando a posição do estado e o ângulo da ação. 
    É possivel ver a utilidade num gradiente de verde e a politica representada por setes amarelas.
    Este método vai ser diferente da classe PlanoPEE, que mostrava apenas o caminho do agente até o alvo mais próximo.
    '''
    def mostrar(self, vista):
        if self.__politica:

            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)

            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)