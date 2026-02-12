from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae.agente.agente import Agente


class AgenteDelibPDM(Agente):

    def __init__(self):
        planeador = PlaneadorPDM()
        controlo = ControloDelib(planeador)
        super().__init__(controlo)