from dataclasses import dataclass #import do módulo dataclass 
from mod.estado import Estado #import da classe Estado
from mod.operador import Operador #import da classe Operador


#estrutura de dados para representar um passo na solução
@dataclass
class PassoSolucao:
    estado: Estado  #estado associado ao passo da solução
    operador: Operador  #operador utilizado para chegar ao estado
