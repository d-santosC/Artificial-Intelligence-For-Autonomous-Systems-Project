from contagem.mod_prob.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade

#TESTE:

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2]

problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

mec_proc = ProcuraProfundidade()

solucao = mec_proc.procurar(problema)

#Mostrar solução
if solucao:
    for passo in solucao:
        print(passo.estado.id_valor(), passo.operador._incremento)