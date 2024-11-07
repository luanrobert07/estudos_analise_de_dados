import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='UTF-8')

print('Questão 1')

colunas = [0,1,2,3]

slicing_colunas = ds[:,colunas]
print(slicing_colunas)

print('Questão 2')

coluna_regiao = [1]

slicing_coluna_região = ds[1:,coluna_regiao]
print(len(np.unique(slicing_coluna_região)))
print(np.unique(slicing_coluna_região))

print("Questão 3")

coluna_literacy = ds[1:,9]
print(coluna_literacy)





total_coluna_literacy = len(coluna_literacy)
coluna_literacy = coluna_literacy.astype(float)
sum_coluna_literacy = np.sum(coluna_literacy)

media_coluna_literacy = np.mean(coluna_literacy)
print(media_coluna_literacy)

taxa_media = (sum_coluna_literacy/total_coluna_literacy)

print("Taxa média", taxa_media )


print("Questão 4")

coluna_paises = ds[1:,0]
coluna_regiao = ds[1:,1]

coluna_regiao_sem_espaço = np.char.strip(coluna_regiao)
coluna_paises_sem_espaço = np.char.strip(coluna_paises)

sum_paises_america_do_norte = np.sum(coluna_regiao_sem_espaço == 'NORTHERN AMERICA')
paises_america_do_norte = coluna_paises_sem_espaço[coluna_regiao_sem_espaço == 'NORTHERN AMERICA']

print(paises_america_do_norte)
print("Paises da America do Norte", sum_paises_america_do_norte)


print("Questão 5")

coluna_per_capita = ds[1:,8]
coluna_paises = ds[1:,0]
coluna_regiao = ds[1:,1]

print(coluna_regiao)

coluna_regiao_sem_espaço = np.char.strip(coluna_regiao)
coluna_paises_sem_espaço = np.char.strip(coluna_paises)

paises_america_sul_caribe = coluna_paises_sem_espaço[coluna_regiao_sem_espaço == 'LATIN AMER. & CARIB']
per_capita_america_sul_caribe = coluna_per_capita[coluna_regiao_sem_espaço == 'LATIN AMER. & CARIB']

indice_maior_per_capita = np.argmax(per_capita_america_sul_caribe)

pais_maior_per_capita = paises_america_sul_caribe[indice_maior_per_capita]

print("Pais com maior per capita da America sul caribe", pais_maior_per_capita)



