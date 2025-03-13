import numpy as np

ds = np.loadtxt('brands.csv', delimiter=';', dtype='str', encoding='utf-8')

print(ds[0, :]) # colunas

colunaBrand = ds[:,0]
colunaValor2021 = ds[1:,10].astype(float)
colunaValor2022 = ds[1:,9].astype(float)

google = np.char.find(colunaBrand, 'Google') != -1

valorizacao = colunaValor2022[3] - colunaValor2021[3]

print("Valorização",valorizacao)


# Exercício 2

brandNameGroup = np.char.find(colunaBrand, 'Group')
print(len(brandNameGroup))

# Exercício 3

firstFiveCompanies = ds[1:6, 0]
valor2022_firstFiveCompanies = ds[1:6, 9].astype(float)
print(firstFiveCompanies)

aumento10Porcento = valor2022_firstFiveCompanies * 1.10
print(aumento10Porcento)

# Exercício 4

slicingColumns = ds[1:, [0, 1, 2]]
print(slicingColumns[slicingColumns[:,2].astype(int) > 2000, 0])

# Exercício 5
anos, contagens = np.unique(ds[1:, 2], return_counts=True)
print("Diferentes anos empresas fundadas", anos)

print("contagem", contagens)

indice_max = np.argmax(contagens)
valor_mais_frequente = anos[indice_max]
frequencia = contagens[indice_max]

print(f"O ano em que mais empresas abriram as portas foi {valor_mais_frequente} com {frequencia} empresas.")







