import numpy as np

#Slicing de dados
# np.random.seed(5)
# arr = np.random.randint(1,10,10)

# arr2 = arr[0:4].copy()
# arr2[0] = 9
# arr2[1] = 9

# print(arr)
# print(arr2)

# Condicionais

# print(arr)
# # mascara de valores booleano
# print(arr<6)
# # mostrando os elementos
# print(arr[arr<6])

# cond = arr%2==1
# print(cond)
# print(arr[cond])

# Subpacote Char do NUmpy (manipulação de textos)

# arr = np.array(['Pedro', 'Ana', 'Tiago', 'Davi', 'Anelise'])

# # Find
# print(np.char.find(arr, 'An')) 

# cond = np.char.find(arr, 'An') >= 0

# print(arr[cond])


# Carregando um dataset

ds = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')
# print(ds)

print('Colunas: ', ds[0, :])

# Quais as diferentes empresas que já fizeram missões espaciais segundo esse dataset?

# extraindo uma coluna
names= len(np.unique(ds[1:,1]))
print(names, "empresas")



