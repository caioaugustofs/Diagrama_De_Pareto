from pareto import Pareto


item = ['A', 'B', 'C', 'D', 'E', 'F']
frequencia = [55, 38, 22, 8, 7, 6]

prt = Pareto(item=item, frequencia=frequencia)

tabela = prt.tabela()

print(tabela)
print(prt.Percentual())
print(prt.Percentual_Acumulado())

prt.plot(save=True)
