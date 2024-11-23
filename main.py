# -*- coding: utf-8 -*-

from pareto import Pareto

item = ['A', 'B', 'C', 'D', 'E', 'F']
frequencia = [55, 38, 22, 8, 7, 6]
label = 'Erros por funcao'

prt = Pareto(item=item, frequencia=frequencia, label=label)

tabela = prt.tabela()

print('\n')
print(prt.__str__())
print('\n')
print(f'Percentual = {prt.Percentual()}')
print(f'Percentual Acumulado = {prt.Percentual_Acumulado()}')
print('\n')
print(tabela)
print('\n')

prt.plot(save=True, title='Diagrama de Pareto - Erros por função', hline=True)
