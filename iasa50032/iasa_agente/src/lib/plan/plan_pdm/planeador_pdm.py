from pdm.pdm import PDM #import da classe PDM
from plan.modelo.modelo_pdm_plan import ModeloPDMPlan #import da classe ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM #import da classe PlanoPDM
from plan.planeador import Planeador #import da interface Planeador 

'''
A classe PlaneadorPDM vai representar um tipo de planeador baseado nos Processos de Decisão de Markov (PDM).
'''

class PlaneadorPDM(Planeador):

    #construtor da classe que vai receber a gama que vai ter um valor por omissão de 0.85, e o delta_max 
    #que vai ter um valor por omissão de 1
    def __init__(self, gama=0.85, delta_max=1):
        self.__gama = gama
        self.__delta_max = delta_max
    
    '''
    método onde vamos planear a trajectória do nosso agente tendo em conta o modelo do mundo e os objectivos.
    Primeiramente criamos um modelo pdm com uma instância da classe ModeloPDMPlan usando os parâmetros modelo_plan e objetivos recebidos.
    De seguida, criamos uma instância da classe PDM usando o modelo pdm e as variáveis gama e delta_max recebidas no construtor.
    Calcula-se a utilidade e a politica através do método resolver().
    Retorna-se o plano criado com a utilidade e a politica calculadas
    '''
    def planear(self, modelo_plan, objectivos):
        if objectivos:

            modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos)
            pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
            utilidade, politica = pdm.resolver()
            return PlanoPDM(utilidade, politica)
        
        return None
            
    #propriedades da classe

    @property
    def gama(self):
        return self.__gama
    
    @property
    def delta_max(self):
        return self.__delta_max