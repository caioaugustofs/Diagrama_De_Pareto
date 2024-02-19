# Diagrama de Pareto

Este repositório implementa uma classe Python Pareto para representar e analisar uma distribuição de Pareto. Ele fornece métodos para criar tabelas de dados e gráficos combinados Seaborn para visualizar a distribuição.

### Args:
* item (list): Lista de itens.
* frequencia (list): Lista de frequências correspondentes aos itens.
* label (str, opcional): Rótulo para o eixo x do gráfico. Padrão: "itens".

~~~python
from pareto import Pareto

item = ['A', 'B', 'C', 'D', 'E', 'F']
frequencia = [55, 38, 22, 8, 7, 6]
label = 'Erros por função'

prt = Pareto(item=item, frequencia=frequencia, label=label)

tabela = prt.tabela()

prt.plot(save=True)
~~~

# Contribuindo

Sinta-se à vontade para contribuir com sugestões, melhorias e correções ao projeto criando um pull request