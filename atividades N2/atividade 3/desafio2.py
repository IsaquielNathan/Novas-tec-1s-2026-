import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Engenheiro de Qualidade",
    layout="wide"
)

st.title("Dashboard do Engenheiro de Qualidade")

np.random.seed(42)

df = pd.DataFrame({
    'Data': np.random.choice(
        pd.date_range('2026-01-01', periods=30), 100
    ),
    'Desenvolvedor': np.random.choice(
        ['Ana', 'Carlos', 'Marina', 'João'], 100
    ),
    'Linhas_Adicionadas': np.random.randint(10, 500, 100),
    'Linhas_Removidas': np.random.randint(5, 300, 100),
    'Bugs_Gerados': np.random.randint(0, 10, 100)
})

dev_selecionado = st.sidebar.radio(
    "Selecione o Desenvolvedor",
    df['Desenvolvedor'].unique()
)

df_filtrado = df[
    df['Desenvolvedor'] == dev_selecionado
]

st.metric(
    "Total de Linhas Adicionadas",
    df_filtrado['Linhas_Adicionadas'].sum()
)

bugs_por_data = df_filtrado.groupby(
    'Data'
)['Bugs_Gerados'].sum().sort_index()

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    bugs_por_data.index,
    bugs_por_data.values,
    marker='o'
)

ax.set_title(f'Bugs Gerados por {dev_selecionado}')
ax.set_xlabel('Data')
ax.set_ylabel('Quantidade de Bugs')

plt.xticks(rotation=45)

st.pyplot(fig)

if st.button("Exibir Desenvolvedor com Maior Média de Bugs"):

    media_bugs = df.groupby(
        'Desenvolvedor'
    )['Bugs_Gerados'].mean()

    st.warning(
        f'Desenvolvedor com maior média de bugs: '
        f'{media_bugs.idxmax()} '
        f'({media_bugs.max():.2f} bugs por commit)'
    )
