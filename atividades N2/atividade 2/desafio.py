import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" 

#Tarefa 1
df = pd.read_csv(url) 

df = df.head()
print (df)

info = df.info()

dimensao = df.shape
print (dimensao)

#Tarefa 2
estatistica = df.describe()
print (estatistica)

classe = df['Pclass'].nunique()
print (classe)

genero = df['Sex'].value_counts()
print (genero)

#Tarefa 3
idade_nome = df.loc[0:10, ['Name', 'Age']]
print (idade_nome)

dados = df.iloc[14:15]
print (dados)

#Tarefa 4 
velhos = df[df['Age']>60]
print (velhos)

ricas = df[(df['Sex']=='female') & (df['Pclass']==1)]
print (ricas)

tarifa = df[(df["Fare"].between(50, 100))]
print (tarifa)

porto = df.query("Embarked == 'C' and Survived == 1")
print (porto)
