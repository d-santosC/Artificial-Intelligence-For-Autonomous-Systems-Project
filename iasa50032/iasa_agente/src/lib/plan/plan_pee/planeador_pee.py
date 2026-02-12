from pee.melhor_prim.procura_aa import ProcuraAA #import da classe ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist #import da classe HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan #import da classe ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE #import da classe PlanoPEE
from plan.planeador import Planeador #import da interface Planeador

'''
PlaneadorPEE vai ser um planeador onde vamos procurar, de uma forma especifica, o melhor caminho para o agente. 
Utiliza o modelo plano e os lugares que queremos ir (objetivos), garantindo o percurso mais eficiente.
Vamos utilizar a procura AA (A*) e a heuristica vai usar uma lista de objetivos ordenados por distância, 
escolhendo primeiro o objetivo mais próximo para que o agente se aproxime mais rapidamente
'''

class PlaneadorPEE(Planeador):

    #construtor onde incializamos a procura A*
    def __init__(self):
        self.__mec_pee = ProcuraAA()
    
    #método onde vamos criar um novo plano
    def planear(self, modelo_plan, objectivos):

        #se temos objetivos vamos criar um plano
        if objectivos:
            estado_final = objectivos[0] #vamos buscar o primeiro objetivo da lista
            problema = ProblemaPlan(modelo_plan, estado_final) #criamos uma instância de ProblemaPlan
            heuristica = HeurDist(estado_final) #criamos uma instância de HeurDist

            solucao = self.__mec_pee.procurar(problema, heuristica) #procuramos uma solução

            #se existir solucao vamos produzir um plano a partir da solucao que foi gerada
            if solucao:
                return PlanoPEE(solucao)