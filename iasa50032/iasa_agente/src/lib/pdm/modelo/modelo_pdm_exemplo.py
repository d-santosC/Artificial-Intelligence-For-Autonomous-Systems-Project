'''
Classe de exemplo de um modelo de Processo de Decisão Markov (PDM).
'''

class ModeloPDMExemplo():

    #método que retorna a lista dos estados possíveis no modelo
    def S(self):
        return [1,2,3,4,5,6,7]

    #método onde definimos o conjunto de ações possiveis para um estado s.
    #se s for 1 ou 7 não temos ações possiveis por são estados terminais (não admitem transições)
    def A(self, s):
        return ['<', '>'] if s not in [1,7] else []

    #método de transição onde determinamos a probabilidade de ir do estado s ao estado sn através da ação a.
    #se s não é 1 nem 7, a transição tem uma probabilidade de 1 (determinística),
    #se s for 1 ou 7, a transição vai ter probabilidade 0, já que não temos ações disponíveis nesses estados
    def T(self, s, a, sn):
        return 1 if s not in [1,7] else 0

    #método da recompensa.
    #se o próximo estado sn é 7, a recompensa vai ser 1 (estado final desejável),
    #se o próximo estado é 1, a recommpensa vai ser -1 (estado indesejável)
    def R(self, s, a, sn):
        return 1 if sn == 7 else -1 if sn == 1 else 0
    
    #método onde retornamos a lista de estados sucessores possíveis ao tomar a ação a através do estado s.
    #se a ação é '<', o próximo estado é s-1, mas não pode ser menor que 1,
    #se a ação é '>', o próximo estado é s+1, mas não pode ser maior que 7
    def suc(self, s, a):
        return [max(1, s-1) if a == '<' else min(7, s+1)]