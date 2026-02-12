from pdm.modelo.modelo_pdm_exemplo import ModeloPDMExemplo
from pdm.pdm import PDM

'''
Classe de teste
'''

gama = 0.5
delta_max = 0
modelo_pdm = ModeloPDMExemplo()
pdm = PDM(modelo_pdm, gama, delta_max)
utilidade, politica = pdm.resolver()

print(utilidade)
print(politica)
    