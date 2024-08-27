# CAP. 4 - NUMPY

import numpy as np

# arr = np.array([1,2,3])
# print(type(arr))
# print(arr)

# mtz = np.array([
#     [1,2,3], 
#     [4,5,6], 
#     [7,8,9]
# ])
# print(mtz)
# print(mtz.size)
# print(mtz.ndim)
# print(mtz.shape)

# mtz = np.arange(1,10,1)
# print(mtz)

# #reshape - transforma estruturas de dados em outro formato
# mtz = mtz.reshape(3, 3)
# print(mtz)

# arr = np.arange(1,10,1)
# arr2 = np.arange(10,19, 1)

# print(arr)
# print(arr2)

# print(arr+arr2)
# print(arr*arr2)

# print(np.concatenate([arr, arr2]))


# # Random
# np.random.seed(5) #semente aleatória -- é possível geral o mesmo número em pc diferente
# arr = np.random.randint(1, 10, 8)

# print(arr)

# # tirando os números repetidos e ordenando
# print(np.unique(arr))

np.random.seed(10)
mtz = np.random.randint(1,20,9).reshape(3,3)

print('Gastos com água -->', mtz.sum(axis=1)[0])
print('Gastos com água em Janeiro -->', mtz.sum(axis=0)[0])

#Broadcasting
print(mtz*0.9)




