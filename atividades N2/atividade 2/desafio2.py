import pandas as pd
df = pd.read_csv(
    "funcionarios.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A","-"]
)

print(df.isnull().sum())
print(df)

df = df.dropna(subset=['salario'])
df['idade'] = df['idade'].fillna(df.groupby('departamento')['idade'].transform('mean'))
df['idade'] = df['idade'].astype('Int64')
print(df.head())

df['data_admissao'] = pd.to_datetime(df['data_admissao'])
df['anos_empresa'] = (pd.Timestamp.now() - df['data_admissao']).dt.days / 365.25
df['anos_empresa'] = df['anos_empresa'].round(1)
print(df.head())

media_salario = df.groupby('departamento')['salario'].transform('mean')
df_filtrado = df[(df['anos_empresa'] > 5) & (df['salario'] < media_salario)]
print(df_filtrado.head())
