from pareto import Pareto


item = ['A', 'B', 'C', 'D', 'E', 'F']
frequencia = [55, 38, 22, 8, 7, 6]
label = 'Erros por função'

prt = Pareto(item=item, frequencia=frequencia, label=label)

tabela = prt.tabela()

print(tabela)
print()
print(f'Percentual = {prt.Percentual()}')
print(f'Percentual Acumulado = {prt.Percentual_Acumulado()}')

print()
print(prt.__str__())
prt.plot(save=True)
