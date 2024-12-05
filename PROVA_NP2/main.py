import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('eletric_cars.csv', delimiter=',')
print(df.head(0))

# Exercício 1
slicingNomeeLink = df.loc[:, ['Car_name', 'Car_name_link', 'Fast_charge']]
carregaMaisRapido = slicingNomeeLink['Fast_charge'].idxmax()

print("Carrega mais rápido",slicingNomeeLink['Car_name'][carregaMaisRapido], slicingNomeeLink['Car_name_link'][carregaMaisRapido])

# Exercício 2

distanciaMedia = df['Range'].mean()
print("Distância média:", distanciaMedia)

# Exercício 3

columnCarName = df['Car_name'] 
carTesla = columnCarName.str.contains('Tesla')
carMaisBarato = df[carTesla]['Price.DE.'].idxmin()

print("Carro mais barato da Tesla:", df['Car_name'][carMaisBarato])

# Exercício 4



# Exercício 5

columnCarName = df['Car_name'] 
carBYD = columnCarName.str.contains('BYD')

velocidade = df[carBYD]['acceleration..0.100.']

quatroCarrosMaisVelozes = velocidade.nlargest(4)

carrosmaisvelozes = df.nlargest(4, 'acceleration..0.100.')
nameCarrosMaisVelozes = df[carBYD]['Car_name']
capacidadeBateriaCarrosMaisVelozes = df[carBYD]['Battery']



plt.scatter(nameCarrosMaisVelozes, capacidadeBateriaCarrosMaisVelozes)
plt.xlabel("Nome dos carros")
plt.ylabel("Capacidade da bateria")

plt.show()