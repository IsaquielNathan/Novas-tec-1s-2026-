import pandas as pd

df = pd.read_csv(
    'vendas.csv', 
    sep=',',
    encoding='utf-8',
    na_values=['N/A', '-']
)

print (df.head(10))
print (df.info())

df["total_venda"] = df["quantidade"] * df["preco_unitario"]
print (df.head())


df_eletronico = df[(df['categoria'] == 'Eletrônicos') & (df['total_venda'] > 1000)]
print (df_eletronico.head())

df_media = df.groupby('cidade')['total_venda'].mean().sort_values(ascending=False)
print(df_media)
