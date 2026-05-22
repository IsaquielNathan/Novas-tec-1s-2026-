import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    'dados_teste_bugs.csv', 
    sep=',',
    encoding='utf-8',
    na_values=['N/A', '-']
)

media = df['Tempo_Resolucao_Horas'].mean()

df.loc[df['Tempo_Resolucao_Horas'] < 0, 'Tempo_Resolucao_Horas'] = media
df['Tempo_Resolucao_Horas'] = df['Tempo_Resolucao_Horas'].fillna(media)

media_por_modulo = df.groupby('Módulo')['Tempo_Resolucao_Horas'].mean().sort_values(ascending=False)

media_por_modulo.plot(kind='bar', color=['#d62728', '#ff7f0e', '#2ca02c'])
plt.title('Tempo Médio de Resolução por Módulo')
plt.xlabel('Módulo')
plt.ylabel('Tempo Médio (Horas)')
plt.xticks(rotation=0)
plt.show()
