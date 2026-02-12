from sae.ambiente.elemento import Elemento #import da classe Elemento

'''
A classe MecDelib vai representar um Mecanismo Deliberativo e utiliza o Modelo do Mundo.
Vai delibrar os objetivos, produzindo uma lista de estados 

Um Mecanismo Deliberativo permite que o agente tome decisões de maneira deliberativa, ou seja,
vai considerar várias opções e avaliar qual a melhor opção antes de agir.
'''

class MecDelib:

    #construtor da classe onde vamos receber e guardar o modelo mundo
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
    
    '''
    método que vai simular o processor de deliberação, retornando os objetivos do agente.
    Primeiramente, criamos uma lista de objetivos para onde o agente se irá mover, vamos percorrer cada estado
    na lista de estado e se o elemento for do tipo Alvo adicionamos á lista de objetivos
    '''
    def deliberar(self):
        objectivos = [estado for estado in self.__modelo_mundo.obter_estados()
                      if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        
        #organizamos os objetivos pela distancia utilizando o método sort
        if objectivos:
            objectivos.sort(key=self.__modelo_mundo.distancia)

        return objectivos