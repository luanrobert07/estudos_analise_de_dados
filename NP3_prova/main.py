import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('artists.csv', delimiter=',')
print(df.head(0)) # columns

# Exercício 1

columnCountry = df['Country']
artistEUACountry = df[df['Country'].str.contains('United States')]
quantidadeArtistasEUA = len(artistEUACountry)
quantidadeTotalArtistas = len(df)

porcentagemEUA = ( quantidadeArtistasEUA/ quantidadeTotalArtistas) * 100
print(f'Porcentagem de artistas dos EUA: {porcentagemEUA:.2f}%')

# Exercício 2

columnPeriodActive = df['period_active']
artistasNãoAtivos = df[columnPeriodActive.str.contains('present') != 1]

print("Nome e período dos artistas que já não mais estão em atividade: ", artistasNãoAtivos[['Artist', 'period_active']])


# Exercício 3

columnYear = df['Year']
discoMaisAntigoID = df.loc[columnYear.idxmin()]

print("Nome e país do artista que lançou o disco mais antigo: ",discoMaisAntigoID[['Artist', 'Country']])


# Exercício 4

columnGenre = df['Genre']
columnCountry = df['Country']
columnRockHardUS = columnGenre.str.contains('hard rock') & columnCountry.str.contains('United States')
bandaVendeuMaisDiscoID = df[columnRockHardUS].loc[df[columnRockHardUS]['Sales'].idxmax()]

melhorBanda = bandaVendeuMaisDiscoID['Artist']

print(f"A banda convidada será a: ", melhorBanda)

