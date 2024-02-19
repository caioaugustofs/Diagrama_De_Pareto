import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Pareto:
    """
    Cria um diagrama de Pareto a partir de dados de itens e frequências.

    Args:
        item (list): Lista de itens.
        frequencia (list): Lista de frequências correspondentes aos itens.
        label (str, opcional): Rótulo para o eixo x do gráfico. Padrão: "itens".

    Retorna:
        Pareto: Objeto Pareto contendo os dados e métodos para gerar o diagrama.
    """

    def __init__(
        self, item: list, frequencia: list, label: str = 'items'
    ) -> None:
        self.item = item
        self.frequencia = frequencia
        self.label = label

    def __repr__(self) -> str:
        """
        Retorna uma representação textual do objeto Pareto.

        Retorna:
            str: Representação textual do objeto.
        """
        return f'Pareto(items={self.item}, frequencies={self.frequencia}, label={self.label})'

    def tabela(self) -> pd.DataFrame:
        """
        Cria uma tabela a partir dos dados de itens e frequências.

        Retorna:
            pd.DataFrame: Tabela contendo os itens, frequências, percentual e percentual acumulado.
        """
        data = pd.DataFrame(
            {self.label: self.item, 'frequencia': self.frequencia}
        )

        data.sort_values('frequencia', ascending=False, inplace=True)
        data['precentual'] = data['frequencia'] / np.sum(data['frequencia'])
        data['precentual_cum'] = np.cumsum(data['precentual'])
        return data

    def Percentual(self) -> list:
        """
        Retorna uma lista com os percentuais de cada item.

        Retorna:
            list: Lista contendo os percentuais de cada item.
        """
        return list(self.tabela()['precentual'])

    def Percentual_Acumulado(self) -> list:
        """
        Retorna uma lista com os percentuais acumulados de cada item.

        Retorna:
            list: Lista contendo os percentuais acumulados de cada item.
        """
        return list(self.tabela()['precentual_cum'])

    def get_text(self, title) -> str:
        """
        Gera o nome do arquivo de imagem para o diagrama.

        Args:
            title (str): Título do diagrama.

        Retorna:
            str: Nome do arquivo de imagem.
        """
        title = title.replace(' ', '_')
        return f'{title}.png'

    def plot(
        self,
        title: str = 'Diagrama de Pareto',
        figsize: tuple = (12, 6),
        save: bool = False,
    ) -> None:
        """
        Gera e exibe um diagrama de Pareto.

        Args:
            title (str, opcional): Título do diagrama. Padrão: "Diagrama de Pareto".
            figsize (tuple, opcional): Tamanho da figura em polegadas. Padrão: (12, 6).
            save (bool, opcional): Indica se o diagrama deve ser salvo em um arquivo. Padrão: False.
        """

        data = self.tabela()

        fig, ax1 = plt.subplots(figsize=figsize)

        sns.barplot(data=data, x=self.label, y='frequencia', ax=ax1)

        ax2 = ax1.twinx()

        sns.lineplot(
            data=data,
            x=self.label,
            y='precentual_cum',
            color='tomato',
            marker='o',
            markersize=8,
            ax=ax2,
        )
        ax1.set_ylabel('Frequência')
        ax2.set_ylabel('Percentual acumulado')
        plt.title(title.upper())

        ax1.grid(ls='-.', linewidth=0.5)

        [tick.set_rotation(45) for tick in ax1.get_xticklabels()]

        if save:
            plt.savefig(
                self.get_text(title=title),
                format='png',
                dpi=500,
                bbox_inches='tight',
            )

        plt.show()
