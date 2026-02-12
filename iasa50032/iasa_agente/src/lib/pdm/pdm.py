from pdm.mec_util import MecUtil #import da classe MecUtil

'''
A classe PDM vai simular um processo de decisão Markov (PDM). Um PDM é uma ferramenta matemática usada para modelar 
situações onde um agente precisa tomar decisões sequenciais num ambiente indeterminado.
Neste processo temos a propriedade de Markov, onde, dado o estado presente, o futuro é independente do passado. 
Ou seja, o próximo estado depende apenas do estado atual, não sendo influenciado por estados anteriores.
A cada transição de estado o agente vai receber uma recompensa, essa recompensa pode ser positiva ou negativa e 
reflete o ganho ou perda associado à ação realizada.

Nesta classe é implementada uma politica comportamental através da política que é uma estratégia que define qual ação 
o agente deve tomar em cada estado.
'''

class PDM:

    #construtor da classe que recebe como parâmetros: modelo, gama e delta_max
    #inicializamos também um novo mecanismo util
    def __init__(self, modelo, gama, delta_max):
       self.__modelo = modelo
       self.__gama = gama
       self.__delta_max = delta_max
       self.__mec_util = MecUtil(self.__modelo, self.__gama, self.__delta_max) #criamos uma instância do mecanismo util
    

    #método onde vamos criar a nossa estratégia para escolher uma ação (politica)
    #vamos retornar a variável politica que vai ter a informação do valor da ação com maior utilidade
    def politica(self, U):
        S = self.__modelo.S #conjunto de estados
        A = self.__modelo.A #conjunto de ações

        politica = {} #a politica vai ser um dicionário

        #percorremos cada estado e verificamos se há ações disponíveis para o estado atual
        for s in S():

            if A(s):
                #através da função max do python, encontramos a melhor ação para o estado s, já que
                #a melhor ação é aquela que vai maximizar a utilidade da ação para o estado s
                melhor_acao = max(A(s), key=lambda a: self.__mec_util.util_accao(s, a, U))

                politica[s] = melhor_acao #guardamos a ação que foi encontrada no dicionário

        return politica
    
    #método onde vamos calcular a utilidade no nosso mecanismo util e a politica para essa utilidade,
    #utilizando o método anterior
    def resolver(self):
        utilidade = self.__mec_util.utilidade() 
        politica = self.politica(utilidade) 

        return utilidade, politica