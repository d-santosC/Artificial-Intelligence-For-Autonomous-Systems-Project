from sae import Controlo #importar interface Comportamento

#Um agente tem um controlo interno, este controlo interno é feito atraves do controlo reactivo.
#Um agente reactivo é composto por conjuntos de reacções, designados comportamentos

#classe do controlo reactivo que implementa a interface Controlo
class ControloReact(Controlo):

    #construtor da classe, onde incializamos um comportamento
    def __init__(self, comportamento):
        self._comportamento = comportamento
        self.mostrar_per_dir = True #mostrar a informação sensorial no painel

    #metodo processar ativa um comportamento com uma percepção para gerar uma ação
    def processar(self, percepcao):    
        return self._comportamento.activar(percepcao)
