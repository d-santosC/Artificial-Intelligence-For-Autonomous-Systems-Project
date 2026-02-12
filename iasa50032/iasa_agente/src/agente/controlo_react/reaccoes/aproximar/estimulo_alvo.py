from ecr.estimulo import Estimulo #import da interface Estimulo
from sae.ambiente.elemento import Elemento #import da classe Elemento

#classe que implementa a interface Estimulo e que tem como objectivo detetar um alvo numa direção recebida
class EstimuloAlvo(Estimulo):

    #construtor da classe, recebe uma direção para verificar se há alvo
    def __init__(self, direccao, gama=0.9):
        self.__direccao = direccao
        self.__gama = gama
    
    #metodo para detetar um elemento no ambiente na direção recebida
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self.__direccao] #obtemos os valores do elemento e da distancia através de descompactação

        #verificar se o elemento é um alvo, se for a intensidade é a multiplicação da gama com a distancia,
        #se  não for a intensidade é 0
        if elemento == Elemento.ALVO:
            
            intensidade = self.__gama ** distancia
            return intensidade
        
        return 0