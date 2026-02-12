from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif #import da classe AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim #import da classe ProcuraMelhorPrim


class ProcuraCustoUnif(ProcuraMelhorPrim):

    #construtor da classe onde vamos inicializar um avaliador que toma decisões pelo custo
    def __init__(self):
        super().__init__(AvaliadorCustoUnif()) #inicializamos a classe AvaliadorCustoUnif