from pee.prof.procura_prof_lim import ProcuraProfLim #import da classe ProcuraProfLim

'''
Esta classe vai ser uma procura em profundidade. Este tipo de procura é um mecanismo
óptimo e completo.

À medida que vamos aumentando o limite de profundidade, o algoritmo realiza a procura
utilizando o limite atual. Se uma solução é encontrada, vamos retorna-la
'''

class ProcuraProfIter(ProcuraProfLim):
     

    '''
    Este método vai procurar até uma profundidade crescente, ajustando a profundidade máxima para o valor
    da profundidade máxima atual e chamando o método de procura da classe ProcuraProfLim, neste caso,
    o método de procura da classe mecanismo de procura.

    Esta procura vai retornar uma solução e, se essa solução não for None, vamos devolver a solução
    e terminar a procura. Caso contrário, vamos incrementar a profundidade máxima em uma unidade
    '''

    def procura(self, problema, inc_prof = 1, limite_prof = 100):

        for profundidade in range(0, limite_prof + 1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)

            if solucao:
                return solucao