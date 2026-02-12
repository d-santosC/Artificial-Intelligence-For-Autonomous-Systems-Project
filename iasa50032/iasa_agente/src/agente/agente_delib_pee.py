from agente.controlo_delib.controlo_delib import ControloDelib #import da classe ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE #import da classe PlaneadorPEE
from sae.agente.agente import Agente #import da classe Agente

'''
A classe AgenteDelibPEE vai representar um agente deliberativo PEE (Procura em Espaço de Estados), 
que é um tipo de agente que vai planear as suas ações com base em objetivos definidos para encontrar as melhores soluções.
Permite tomar decisões flexíveis e adaptativas.
'''

class AgenteDelibPEE(Agente):

    #construtor onde inicializamos um planeador do tipo PEE, inicializamos um controlado deliberativo com esse planeador
    #e inicializamos o construtor da superclasse com o controlo criado
    def __init__(self):
        planeador = PlaneadorPEE()
        controlo = ControloDelib(planeador)
        super().__init__(controlo)