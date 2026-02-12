from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

'''
A classe ModeloPDMPlan vai ser utilizada para modelar e resolver problemas que envolvem os Processos de Decisão de Markov (PDM).
Vai implementar duas interfaces ModeloPDM e ModeloPlan.
'''

class ModeloPDMPlan(ModeloPlan, ModeloPDM):
     
    #construtor da classe que vai receber o modelo_plan, objectivos e o rmax com valor por omissão de 1000
    #é criado também um dicionário __transicoes que regista todas as possíveis transições entre estados com base nas ações disponíveis
    def __init__(self, modelo_plan, objectivos, rmax=1000):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
        self.__transicoes = {(s, a): a.aplicar(s) for s in self.obter_estados() for a in self.obter_operadores()}

    #método que retorna o estado atual do modelo
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    #método que retorna a lista de estados do modelo
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    #método que retorna a lista de operadores do modelo
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    #método que vai representar o S, ou seja o conjunto de estados do mundo
    def S(self):
        return self.obter_estados()
    
    #método que vai representar o A, ou seja o conjunto de acções possíveis num estado
    def A(self, s):
        return self.obter_operadores() if s not in self.__objectivos else []
    
    #método que vai representar o T, ou seja a probabilidade de transição de s para sn através de a
    #como estamos num ambiente determinista a probabilidade vai ser 1
    def T(self, s, a, sn):
        return 1 if self.__transicoes.get((s, a)) == sn else 0
    
    #método que vai representar o R, ou seja a recompensa esperada na transição de s para sn através de a
    #A recompensa é calculada a partir do custo (é negativo porque está em movimento)
    def R(self, s, a, sn):
        return self.__rmax if sn in self.__objectivos else -a.custo(s, sn)
    
    #método que vai retornar o estado sucessor a partir do dicionário de transições
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []