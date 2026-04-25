# -*- coding: utf-8 -*-

from pareto import Pareto


item = ['A', 'B', 'C', 'D', 'E', 'F','G']
frequencia = [55, 38, 22, 8, 7, 6, 10]
label = 'Erros por funcao'

prt = Pareto(item=item, frequencia=frequencia, label=label)

tabela = prt.tabela()

print('\n')
print(prt)
print('\n')
print(f'Percentual = {prt.percentual()}')
print(f'Percentual Acumulado = {prt.percentual_acumulado()}')
print('\n')
print(tabela)
print('\n')

prt.plot(save=True,
         title="Diagrama de Pareto - Erros por função", 
         hline=True)
