from sae.ambiente.direccao import Direccao
from .resposta.resposta_mover import RespostaMover #import da classe RespostaMover
from ecr.comportamento import Comportamento #import da classe Comportamento
 #import da classe Direccao

''' 
Comportamento que conta o numero de passos que o agente já deu, quando chegar a 10 passos move-se para norte
'''

class ContarPassos(Comportamento):

    def __init__(self):
        self.__passos = 0 #numero de passos
        self.__resposta = RespostaMover(Direccao.NORTE) #criar uma resposta para mover para a direção Norte

    def ativar(self, percepcao):
        self.__passos += 1 #contar mais 1 passo
        print(self.__passos) #imprimir o número de passos

        #verificamos se o número de passos é maior ou igual a 10
        if self.__passos >= 10:
            return self.__resposta.activar(percepcao) #retorna a resposta de mover para na direção Norte
