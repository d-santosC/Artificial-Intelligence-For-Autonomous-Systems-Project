from agente.agente_delib_pdm import AgenteDelibPDM
from agente.agente_delib_pee import AgenteDelibPEE
from sae import Agente
from sae import Simulador
from agente.agente_reactivo import AgenteReactivo as Agente #import onde passamos o agente reactivo para agente

#from agente.agente_reactivo import AgenteDelib as Agente

print("teste")

Simulador(4, AgenteDelibPDM()).executar()