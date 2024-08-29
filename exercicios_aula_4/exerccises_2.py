import numpy as np
from collections import Counter

# Number 1

np.random.seed(5)

float_array = np.random.uniform(-1, 1, 10)

multiplied_array = float_array * 100

integer_array = np.floor(multiplied_array).astype(int)

print("Array original:", float_array)
print("Array multiplicado por 100:", multiplied_array)
print("Array com a parte inteira:", integer_array)


# Number 2

np.random.seed(10) 
mtz = np.random.randint(1, 51, size=(4, 4))
print(mtz)

# NUmber 3
media_linhas = np.mean(mtz, axis=1)

media_colunas = np.mean(mtz, axis=0)

maior_media_linha = np.max(media_linhas)
maior_media_coluna = np.max(media_colunas)

print("Matriz:")
print(mtz)
print("\nMédias das linhas:", media_linhas)
print("Médias das colunas:", media_colunas)
print("\nMaior média das linhas:", maior_media_linha)
print("Maior média das colunas:", maior_media_coluna)


# Number 4

# Contar a quantidade de aparições de cada número
contador = Counter(mtz.flatten())

# Filtrar os números que aparecem exatamente 2 vezes
numeros_2_vezes = [numero for numero, count in contador.items() if count == 2]

print("Matriz:")
print(mtz)
print("\nContagem de aparições de cada número:")
print(contador)
print("\nNúmeros que apareceram exatamente 2 vezes:", numeros_2_vezes)