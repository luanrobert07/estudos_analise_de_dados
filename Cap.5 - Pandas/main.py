import pandas as pd
import numpy as np

#Series
## array unidimensionais (1-D)
## Lista de labels e lista de valores (um dicionário)

# dic = {'a':10,'b':20, 'c':30}
# s1 = pd.Series(dic)
# s2 = pd.Series(data=[20,30,40,50], index=['a','b','d','e'])

# print(s1.add(s2, fill_value=0))
# print(s1)
# print(s1['b'])
# print(s1[['a', 'c']])

#condicional
# print(s2[s2 <= 30])


#DataFrames

## Duas ou mais dimensões (2-D+)
## Uma coleção de labels e uma coleção de colunas
## Planilha de excel

# np.random.seed(5)
# df = pd.DataFrame(data=np.random.randint(1,10,[3,3]), index=['x','y','z'], columns=['a','b','c'])
# print(df)
# print(df['b']['y']) #elemento único
# print(df[['a','c']]) #colunas específicas

#Slicing na matriz loc e iloc
# print(df.loc[['y','z'], ['b','c']])
# print(df.iloc[1:,1:])


#Carregamento de dataset

df = pd.read_csv('paises.csv',delimiter=';')
print(df.columns)
print(df.head(3))
print(df.tail(4))


