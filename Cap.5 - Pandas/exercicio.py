import pandas as pd
import numpy as np


df = pd.read_csv('paises.csv',delimiter=';')

regionColumn = df['Region']

regionOceania = regionColumn.str.contains('OCEANIA')

paises_oceania = df[regionOceania]['Country']
quantPaíses = len(paises_oceania)

print('Países da Oceania: ')
print(paises_oceania)
print('Quantidade de países na Oceania: ', quantPaíses)


print('Média da taxa de alfabetização(%): ', df['Literacy (%)'].mean())


idMaiorPopulação = df['Population'].idxmax()

print('Maior população: ', df['Population'][idMaiorPopulação])
print('Nome do país com mais população: ', df['Country'][idMaiorPopulação])
print('Nome da região com maior população: ', df['Region'][idMaiorPopulação])

noCoast = df[df['Coastline (coast/area ratio)'] == 0]
noCoastCoutry = noCoast['Country'].copy()
noCoastCoutry.to_csv('noCoast.cvs')

