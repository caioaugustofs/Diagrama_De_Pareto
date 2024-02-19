import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Pareto:
    def __init__(self, item: list, frequencia: list) -> None:
        self.item = item
        self.frequencia = frequencia

    def __repr__(self) -> str:
        return f'Pareto(items={self.item}, frequencies={self.frequencia})'

    def tabela(self) -> pd.DataFrame:

        data = pd.DataFrame(
            {'items': self.item, 'frequencia': self.frequencia}
        )

        data.sort_values('frequencia', ascending=False, inplace=True)
        data['precentual'] = data['frequencia'] / np.sum(data['frequencia'])
        data['precentual_cum'] = np.cumsum(data['precentual'])
        return data

    def Percentual(self) -> list:
        return list(self.tabela()['precentual'])

    def Percentual_Acumulado(self) -> list:
        return list(self.tabela()['precentual_cum'])

    def title_Grafico(self, title) -> str:
        title = title.replace(' ', '_')
        return f'{title}.png'

    def plot(
        self,
        title: str = 'Grafico pareto',
        figsize: tuple = (12, 6),
        save: bool = False,
    ) -> None:

        data = self.tabela()

        fig, ax1 = plt.subplots(figsize=figsize)

        sns.barplot(data=data, x='items', y='frequencia', ax=ax1)

        ax2 = ax1.twinx()

        sns.lineplot(
            data=data,
            x='items',
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
                self.title_Grafico(title=title),
                format='png',
                dpi=500,
                bbox_inches='tight',
            )

        plt.show()
