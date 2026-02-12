from ecr.estimulo import Estimulo #importe da interface Estimulo
from sae.ambiente.elemento import Elemento #import da classe Elemento


#classe que implementa a interface Estimulo e que tem como objetivo detetar um obstaculo numa direção recebida
class EstimuloObst(Estimulo):

    #construtor da classe, recebe uma direção para verificar se há obstaculo
    #a intensidade será retornada caso houver contacto com um obstáculo
    def __init__(self, direccao, intensidade=1):
        self.__direccao = direccao
        self.__intensidade = intensidade
    
    #metodo para detetar um elemento no ambiente na direção recebida
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self.__direccao] #obtemos os valores do elemento e da distancia através de descompactação

        #verificamos se o elemento recebido é um obstáculo, se for retorna a intensidade igual a 1 se não retorna 0
        if elemento is Elemento.OBSTACULO:

            return self.__intensidade
        
        return 0