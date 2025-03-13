import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv', delimiter=',')
print(df.head(0))

#Exercise 01

fast_charge = df['Fast_charge'].min()
carros_rapidos = df[df['Fast_charge'] == fast_charge]
print(f"Carros: {carros_rapidos['Car_name'].values} - Links: {carros_rapidos['Car_name_link'].values}")

#Exercício 02

distanciaMedia = df['Range'].mean()
print("Distância média:", distanciaMedia)

#Exercício 03

colunmNameTesla = df[df['Car_name'].str.contains('Tesla')]
carBarato = colunmNameTesla.min()
print("Carro mais barato da Tesla:", carBarato['Car_name'])


#Exercício 04

carros_rapidos = df.loc[df['acceleration..0.100.'] == df['acceleration..0.100.'].min()]
carros_lentos = df.loc[df['acceleration..0.100.'] == df['acceleration..0.100.'].max()]

df_concat = pd.concat([carros_rapidos, carros_lentos])

plt.bar(df_concat['Car_name'], df_concat['acceleration..0.100.'])
plt.xlabel('Carros')
plt.ylabel('acceleration..0.100.')
plt.show()

#Exercício 05

carBYD = df['Car_name'].str.contains('BYD')
velocidade = df[carBYD]['acceleration..0.100.']
quatroCarrosMaisVelozes = velocidade.nlargest(4)

carrosmaisvelozes = df.nlargest(4, 'acceleration..0.100.')
nameCarrosMaisVelozes = df[carBYD]['Car_name']
capacidadeBateriaCarrosMaisVelozes = df[carBYD]['Battery']

plt.scatter(nameCarrosMaisVelozes, capacidadeBateriaCarrosMaisVelozes)
plt.xlabel("Nome dos carros")
plt.ylabel("Capacidade da bateria")

plt.show()