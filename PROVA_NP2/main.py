import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('eletric_cars.csv', delimiter=',')

# Exercício 1
slicingNomeeLink = df.loc[:, ['Car_name', 'Car_name_link']]
carregaMaisRapido = [slicingNomeeLink['Fast_charge'].max()]

print(carregaMaisRapido)


# Exercício 2

distanciaMedia = df['Range'].mean()
print(distanciaMedia)

# Exercício 3

columnPrice = df['Price.DE.']
carMaisBarato = columnPrice.min()

print(carMaisBarato)

# Exercício 4



# Exercício 5

columnCarName = df['Car_name'] 
carBYD = columnCarName.str.contains('BYD')
quatroCarrosMaisVelozes = carBYD[df.nlargest(4, 'acceleration..0.100.')]
capacidadeBateriaQuatroCarrosMaisVelozes = quatroCarrosMaisVelozes['Battery']

plt.scatter(quatroCarrosMaisVelozes['Car_name'], quatroCarrosMaisVelozes['Battery'])