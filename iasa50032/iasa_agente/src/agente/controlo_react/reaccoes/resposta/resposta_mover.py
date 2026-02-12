from ecr.resposta import Resposta #importar class Resposta
from sae import Accao #importar class Accao

#classe responsavel por realizar a ação do movimento na direção indicada no construtor
#utilizamos tudo oque foi feito da classe Resposta e adicionamos uma direção

'''
RespostaMover extende da classe Resposta que permite a movimentação do agente.
Esta classe permite processar respostas que irão gerar uma ação
Estes movimentos são feitos através de direções, que se encontram no enumerado Direccao
Temos 4 movientos possiveis (norte, sul, este e oeste)
'''
class RespostaMover(Resposta):

    #construtor da classe
    def __init__(self, direccao):
        accao = Accao(direccao) #criar uma instância da classe Accao com uma direccao especifica
        super().__init__(accao) #chamamos o construtor da classe Resposta com a accao anterior como argumento