import numpy as np

# Carregando o dataset
ds = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')

print('Exercício 1')

# Obtendo o número total de missões
total_missoes = ds.shape[0]
print(total_missoes)
print('colunas', ds[0, :])

# Contando o número de missões bem-sucedidas
missoes_bem_sucedidas = np.sum(ds[:, -1] == 'Success')

# Calculando a porcentagem de missões bem-sucedidas
porcentagem_sucesso = (missoes_bem_sucedidas / total_missoes) * 100
print(f"Porcentagem de missões bem-sucedidas: {porcentagem_sucesso:.2f}%")



print('Exercício 2')

# Extraindo a coluna de custos
custos = ds[:, -2]

custos_validos = []

for custo in custos:
    try:
        custo_float = float(custo)
        if custo_float > 0:
            custos_validos.append(custo_float)
    except ValueError:
        continue

# Calculando a média dos custos válidos
if custos_validos:
    media_gastos = np.mean(custos_validos)
    print(f"Média de gastos de uma missão espacial: ${media_gastos:.2f}")
else:
    print("Não há missões com custos válidos.")


print('Exercício 3')

# Contando o número de missões realizadas pelos EUA
missoes_eua = np.sum(np.char.find(ds[:, 2], 'USA') != -1)

print(f"Número de missões realizadas pelos EUA: {missoes_eua}")

print('Exercício 4')

# Filtrando as missões da SpaceX
spacex_missoes = ds[ds[:, 1] == 'SpaceX']
print(spacex_missoes)

# Extraindo os custos
custos = spacex_missoes[:, -2]

# Inicializando variáveis para encontrar a missão mais cara
maior_custo = 0
missao_mais_cara = None

# Percorrendo as missões da SpaceX para encontrar a mais cara
for i, custo in enumerate(custos):
    try:
        custo_float = float(custo)  
        if custo_float > maior_custo: 
            maior_custo = custo_float
            missao_mais_cara = spacex_missoes[i] 
    except ValueError:
        continue

# Exibindo a missão mais cara
if missao_mais_cara is not None:
    print(f"A missão mais cara da SpaceX foi:")
    print(f"Nome: {missao_mais_cara[4]}") 
    print(f"Custo: ${maior_custo:.2f}")
else:
    print("Não há missões válidas da SpaceX com custo.")


print('Exercício 5')

# Inicializando um dicionário para contar as missões por empresa
missões_por_empresa = {}

# Percorrendo as linhas do dataset
for linha in ds:
    empresa = linha[1]  
    if empresa in missões_por_empresa:
        missões_por_empresa[empresa] += 1  
    else:
        missões_por_empresa[empresa] = 1  

print("Quantidade de missões por empresa:")
for empresa, quantidade in missões_por_empresa.items():
    print(f"{empresa}: {quantidade} missões")