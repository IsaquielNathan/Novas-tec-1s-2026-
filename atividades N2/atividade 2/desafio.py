import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" 

#Tarefa 1
filtro = pd.read_csv(url) 

df = filtro.head()
print (df)

info = filtro.info()

dimensao = filtro.shape
print (dimensao)

#Tarefa 2
estatistica = filtro.describe()
print (estatistica)

classe = filtro['Pclass'].nunique()
print (classe)

genero = filtro['Sex'].value_counts()
print (genero)

#Tarefa 3
idade_nome = filtro.loc[0:10, ['Name', 'Age']]
print (idade_nome)

dados = filtro.iloc[14:15]
print (dados)

#Tarefa 4 
velhos = filtro[filtro['Age']>60]
print (velhos)

ricas = filtro[(filtro['Sex']=='female') & (filtro['Pclass']==1)]
print (ricas)

tarifa = filtro[(filtro["Fare"].between(50, 100))]
print (tarifa)

porto = filtro.query("Embarked == 'C' and Survived == 1")
print (porto)
