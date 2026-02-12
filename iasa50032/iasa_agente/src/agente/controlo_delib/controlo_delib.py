from agente.controlo_delib.mec_delib import MecDelib #import da classe MacDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo #import da classe ModeloMundo
from sae.agente.controlo import Controlo
from sae.ambiente.elemento import Elemento #import da classe Controlo



class ControloDelib(Controlo):

    '''
    construtor da classe onde guardamos um planeador recebido, inicializamos um objeto do tipo ModeloMundo,
    e um mecanismo de deliberação com o modelo do mundo, uma lista de objetivos e um plano
    '''
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo() #criar um instância de ModeloMundo
        self.__mec_delib = MecDelib(self.__modelo_mundo) #criar uma instância de MecDelib tendo em consideração o mundo criado
        self.__objectivos = []
        self.__plano = None

    '''
    método que irá representar o processo geral de tomada de decisão e ação.
    
    Primeiramente vamos pegar na percepcao recebida e vamos atualizar o modelo do mundo com base nas perceções
    que o agente obteve, depois com o reconsiderar verificamos se o mundo alterou e se é necessário alterar as opções.
    Se houve alterações vamos deliberar para saber quais são os objetivos a cumprir e planear qual 
    a melhor maneira de atingir o objetivo e gerar um plano de ação
    '''
    def processar(self, percepcao):

        self.__assimilar(percepcao) #com o assimilar vamos atualizar o modelo do mundo

        if self.__reconsiderar():

            self.__deliberar()
            self.__planear()

        self.__mostrar() #vamos mostrar a informação 
        return self.__executar() #executamos o plano que foi gerado

    #método que vai atualizar o modelo consuante a percepção recebida
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
    
    #método onde iremos reconsiderar apenas se não tivermos plano e se o modelo mundo foi alterado
    def __reconsiderar(self):
        return self.__plano is None or self.__modelo_mundo.alterado
    
    #método onde vamos atualizar a lista de objetivos
    def __deliberar(self):
        self.__objectivos = self.__mec_delib.deliberar()
    
    #método onde vamos gerar um plano de ação, para isso temos de verificar se a lista de objetivos não se encontra vazia
    #se a lista estiver vazia não podemos gerar um plano porque não temos objetivos
    def __planear(self):
        self.__plano = self.__planeador.planear(self.__modelo_mundo , self.__objectivos)
        
            
    #método que vai retornar uma ação caso haja um plano
    def __executar(self):
        if self.__plano:
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao
            else:
                self.__plano = None #se não temos operador anulamos o plano

    #método que vai permitir a visualização
    def __mostrar(self):
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)

        #se temos plano vamos mostrar o plano
        if self.__plano:
            self.__plano.mostrar(self.vista)

        #se temos objetivos vamos mostrar cada objetivo
        if self.__objectivos:
            for objectivo in self.__objectivos:
                self.vista.marcar_posicao(objectivo.posicao)

