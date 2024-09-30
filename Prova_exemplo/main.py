import numpy as np

# Carregando o dataset
ds = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8')
print('Colunas: ', ds[0, :])

print('Exercício 1')

column_indices = [0, 1, 2, 3]

slicing = ds[:, column_indices]

print(slicing)

print('Exercício 2')

regioes = ds[:,1]

regioes_unicas = np.unique(regioes)

print(regioes_unicas)
print(len(regioes_unicas), 'Regiões únicas')


print('Exercício 3')

literacy = ds[:,9]
print(literacy)

literacy = literacy[1:] #remove primeira linha

literacy = literacy.astype(float) 

quantidadeLiteracy = len(literacy)
print(quantidadeLiteracy)

sumLiteracy = np.sum(literacy)

mediaLiteracy = sumLiteracy/quantidadeLiteracy

print('Taxa média de alfabetização: ', mediaLiteracy, '%')

print('Exercício 4')

regioes = ds[:,1]
regioes_nothing_space = np.char.strip(regioes)
print(regioes_nothing_space)

countryNorthernAmerica = np.sum(regioes_nothing_space == 'NORTHERN AMERICA') 
print('Paises da América do Norte', countryNorthernAmerica)


print('Exercício 5')

regioes = ds[:, 1]
gdp_per_capita = ds[:, 8]  
countries = ds[:, 0]

regioes_nothing_space = np.char.strip(regioes)

latin_america = regioes_nothing_space == 'LATIN AMER. & CARIB'

latin_american_countries = countries[latin_america]
latin_american_gdp = gdp_per_capita[latin_america]

latin_american_gdp = latin_american_gdp.astype(float)

max_gdp_index = np.argmax(latin_american_gdp)

country_with_max_gdp = latin_american_countries[max_gdp_index]

print('País da América do Sul e Caribe com maior renda per capita:', country_with_max_gdp)

