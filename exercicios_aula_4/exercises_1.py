import numpy as np

# linspace -- gerar números iguamente espaçados
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

# Number 1
arr = np.linspace(0,1,21)
print(arr)

# Number 2
arr1 = np.arange(0,52,2)
arr2 = np.arange(100,49,-2)
concat = np.concatenate([arr1, arr2])

print(np.sort(concat))

# Number 3

print(np.sort(concat) [::-1])

# Number 4

mtz = np.ones((3, 4))
print(mtz)

array_1d = mtz.ravel()

print(array_1d)

# Number 5






