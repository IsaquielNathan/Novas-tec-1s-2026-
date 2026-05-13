import pandas as pd
<<<<<<< HEAD

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
=======
import numpy as np

>>>>>>> f883e5751b2ad0e2c7bd54737a73604b4c9b66c8
