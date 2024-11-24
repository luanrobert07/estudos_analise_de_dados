import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')

#Exercicio 1

dfPaisesColumns = dfPaises.loc[:,['Country', 'Region', 'Population', 'Area (sq. mi.)']]

print(dfPaisesColumns)



#Exercício 2

regionColumn = dfPaises['Region'].unique()

print(len(regionColumn))
print(regionColumn)

#Exercício 3

print(dfPaises['Literacy (%)'].mean())

#Exercício 4

regionColumn = dfPaises['Region']
regionNorthernAmerica = regionColumn.str.contains('NORTHERN AMERICA')

countryNorthernAmerica = dfPaises[regionNorthernAmerica]['Country']

print(len(countryNorthernAmerica))

#Exercício 5

regionColumn = dfPaises['Region']
regionLatinAmericaeCaribe = regionColumn.str.contains('LATIN AMER. & CARIB')
countryLatinAmericaeCaribe = dfPaises[regionLatinAmericaeCaribe]['Country']
countryLatinAmericaeCaribeID = dfPaises[regionLatinAmericaeCaribe]['GDP ($ per capita)'].idxmax()

print(countryLatinAmericaeCaribeID)
print(countryLatinAmericaeCaribe[countryLatinAmericaeCaribeID])
