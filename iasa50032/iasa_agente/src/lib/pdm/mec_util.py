
'''
A classe MecUtil vai ser onde se vai calcular a utilidade de cada estado num processo PDM(Processo Decisão Markov). 
'''

class MecUtil:

    #construtor da classe que recebe como parâmetros: modelo, gama e delta_max
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
    

    '''
    Neste método realizamos os cálculos para saber o valor da utilidade.

    U vai ser um dicionário onde cada estado é inicializado com valor zero.
    u_ant vai ser o valor da utilidade anterior
    Vamos percorrer cada estado no dicionário U e para cada estado vamos calcular a utilidade considerando todas as suas ações.
    Calculamos o delta (diferença) entre os valores de utilidade atual e anterior, isto ocorre até que o delta seja menor 
    que o valor de delta_max.
    '''
    def utilidade(self):
        S = self.__modelo.S #conjunto de estados
        A = self.__modelo.A #conjunto de ações

        #U[s] = 0.0 para todos os estados s na lista de estados S
        U = {s:0.0 for s in S()}

        #fazemos o processo todo enquanto o delta for maior que o delta_max
        while True:
            U_ant = U.copy() #criamos uma copia da utilidade atual para poder comparar
            delta = 0

            #percorremos cada estado na lista de estados
            for s in S():
                #if A(s):
                U[s] = max([self.util_accao(s, a, U_ant) for a in A(s)], default = 0)
                # else:
                #     U[s] = 0
                
                delta = max(delta, abs(U[s] - U_ant[s])) #o delta vai ter o valor da maior diferença encontrada

            #verificamos se o delta é menor que o delta_max
            if delta <= self.__delta_max:
                break

        return U        

    #este método é onde iremos fazer o somatório das utilidades de cada ação
    def util_accao(self, s, a, U):
        T = self.__modelo.T
        R = self.__modelo.R
        suc = self.__modelo.suc
        gama = self.__gama

        return sum(T(s,a,sn) * (R(s,a,sn) + gama * U[sn]) for sn in suc(s,a))
        
    #propriedades da classe:

    @property
    def delta_max(self):
        return self.__delta_max
    
    @property
    def gama(self):
        return self.__gama