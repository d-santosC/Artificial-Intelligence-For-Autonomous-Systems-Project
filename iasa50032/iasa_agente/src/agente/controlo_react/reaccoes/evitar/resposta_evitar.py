from random import choice #import da ferramenta choice
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover #import da classe RespostaMover
from sae.ambiente.direccao import Direccao #import da classe Direccao

'''
Esta classe vai verificar se há obstaculos para evitar, se houverem vê se existe alguma direção livre e se houver, 
move-se para essa direção. Se não houverem obstaculos continua o seu movimento
'''

class RespostaEvitar(RespostaMover):

    #construtor da classe que tem como argumento uma direção inicial que por omissão é ESTE
    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)
        self.__direccoes = list(Direccao) #ficamos com todas as direções 

    '''
    método que executa várias verificações de uma perceção recebida
    se estiver ele escolhe aleatoriamente uma direção
    Se nenhuma direção estiver livre, o método para de ser executado
    '''
    def activar(self, percepcao, intensidade):

        #primeiro verificamos se há contacto com um obstáculo, se não houver, ativa a resposta na direção atual
        if percepcao.contacto_obst(self._accao.direccao): 

            #verifica se há direções livres na lista através do metodo __direccao_livre
            #Correção 1: Não é necessário verificar se é diferente de none, no python é implicito
            if self.__direccao_livre(percepcao):
                self._accao.direccao = self.__direccao_livre(percepcao) #vai mudar a direção para a direção livre
                #Correção 2: return super().activar(percepcao, intensidade), evitar redundancia
            else:
                return None
            
        return super().activar(percepcao, intensidade) #ativamos a resposta
        
    #método para criar uma lista e adicionar a direção livre
    #escolhe uma direção aleatoria da lista
    #vamos ver as direções disponiveis e verificar quais delas estão livres adicionando á lista
    def __direccao_livre(self, percepcao):

        #Correção: no python podemos fazer o ciclo diretamente numa lista
        direccoes = [direccao for direccao in self.__direccoes if not percepcao.contacto_obst(direccao)] #lista das direções livres
        return choice(direccoes) #damos return de uma direção aleatoria 