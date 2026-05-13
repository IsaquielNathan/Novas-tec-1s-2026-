import pandas as pd

df_estoque = pd.read_csv(
    'estoque_atual.csv', 
    sep=',', 
    encoding='utf-8', 
    na_values=['N/A', '-']
)

df_produtos = pd.read_csv(
    'produtos.csv', 
    sep=',', 
    encoding='utf-8', 
    na_values=['N/A', '-']
)

df_vendas = pd.read_csv(
    'vendas_mensal.csv', 
    sep=',', 
    encoding='utf-8', 
    na_values=['N/A', '-']
)

df_merge = pd.merge(df_estoque, df_produtos, on='produto_id', how='inner')
df_completo = pd.merge(df_merge, df_vendas, on='produto_id', how='left')

df_completo['quantidade_vendida'] = df_completo['quantidade_vendida'].fillna(0)

print(df_completo.head(10))
print(df_completo.info())

df_completo['custo_total_estoque'] = df_completo['quantidade'] * df_completo['preco_custo']
df_completo['valor_venda_mes'] = df_completo['quantidade_vendida'] * df_completo['preco_custo'] * 1.5
print(df_completo.head())

df_estoque_zerado = df_completo[df_completo['quantidade'] <= 0]
print(df_estoque_zerado.head())

df_venda_maior = df_completo[df_completo['quantidade_vendida'] > df_completo['quantidade']]
print(df_venda_maior.head())

df_completo['estoque_critico'] = (df_completo['quantidade'] < 10).astype(int)
df_completo['margem_bruta'] = df_completo['valor_venda_mes'] - (df_completo['quantidade_vendida'] * df_completo['preco_custo'])

df_resumo = df_completo.groupby('categoria').agg({
    'quantidade': 'sum',
    'quantidade_vendida': 'sum',
    'estoque_critico': 'sum',
    'margem_bruta': 'sum'
})

print(df_resumo)